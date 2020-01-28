#include <iostream>
#include <memory>
#include <unordered_map>
#include <chrono>
#include <forward_list>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <deque>
#include <vector>



using namespace std;


struct Vertex{

    explicit Vertex(bool _ispipe = false):is_pipe(_ispipe){}
    string tag;
    string id;
    string type;
    string dwg;
    //string pos;

    bool is_pipe;

    bool operator==(const Vertex& rhs) const {return this->id == rhs.id;}
};
struct Pipe : public Vertex
{
    Pipe():Vertex(true){}
};
struct Other : public Vertex
{
    Other():Vertex(false){}
};

struct hashVertex{
    size_t operator()(const Vertex& v) const{
        hash<string> hstr;
        return hstr(v.id);
    }
};
using AdjacencyList = forward_list<Vertex>;
using Graph = unordered_map<Vertex,AdjacencyList,hashVertex>;

const char * usage = "\
PF3 - read and navigate through PF3 data\n\
usage: PF3 <file name>\n\
commands:\n\
    f <id> : list adjacency list of of element <id>\n\
    h      : print this help\n\
    p <start id> <end id> [1..N]<allowed drawings> q [0..N]<excluded connectors> q\n\
           : creates a sub-graph containing all paths that connect <start id> to <end id>,\n\
             searching only in the <allowed drawings> list and breaking at <excluded connectors>.\n\
    q      : quit\n";

void AddRootVertex(Graph& G, const Vertex& u){

    auto it = G.find(u);

    if( it == G.end() ){
        AdjacencyList L;
        G.insert( pair<Vertex,AdjacencyList>(u,L) );
    }
}

void AddVertex(Graph& G, const Vertex& u, const Vertex& v)
{
    auto it = G.find(u);

    if( it != G.end() ){

        AdjacencyList& L = it->second;
        if ( find( L.begin(),L.end(), v ) == L.end() )
            it->second.push_front(v);
        return;
    }

    cout << "Error: u is not root vertex.\n";
}

bool IsPipe( const string& type)
{
    string pl[] = { "Conditioned Air Return",
                           "Secondary Piping",
                           "Primary Piping",
                           "OPC",
                           "Ventilation",
                           "Capillary",
                           "Hydraulic",
                           "Exhaustion",
                           "Connect to Process",
                           "Conditioned Air Supply",
                           "Hose",
                           "Pipe-in-Pipe",
                           "Tubing",
                           "Pneumatic Binary"};

   if ( find( begin(pl), end(pl), type ) != end(pl) ) return true;
   else return false;
}

void CreateGraphFromCSV(Graph& G, ifstream& file, int readtype)
{
    if ( readtype == 0) return;

    file.clear();
    file.seekg(0, ios::beg);

    auto begin = clock();
    string line;
    int counter = 0;
    getline(file,line);

    while ( getline(file,line))
    {
        if (line =="") continue;
        stringstream ss(line);
        string s, pos;
        Pipe pipe;
        Other other;

        getline(ss, pipe.tag, ';');
        getline(ss, pipe.id, ';');
        getline(ss, pipe.type, ';');
        getline(ss, s, ';');
        getline(ss, pipe.dwg, ';');
        //other.dwg = pipe.dwg = s;

        getline(ss, other.tag, ';');
        getline(ss, other.id, ';');
        getline(ss, pos, ';');
        getline(ss, other.type, ';');

        if ( readtype == 3 ) AddRootVertex(G,pipe);
        if ( readtype == 2 ) AddRootVertex(G,other);
        if ( readtype == 1 ) {

            auto it = G.find(other);
            if (it->first.is_pipe)
            {
                other.is_pipe = true;
                other.dwg = it->first.dwg;
            }

            //if ( IsPipe(other.type) ) other.is_pipe = true;)
            // make it a directed graph
            if ( pos == "" )
            {
                AddVertex(G,pipe,other);
                AddVertex(G,other,pipe);
            }
            if ( pos == "To" || pos == "Out" || pos == "OPC" )
                AddVertex(G,pipe,other);

            // "Other" itens doesnt list their adjecency, but its possible to know it
            // inderictly: when a pipe reports a "other" in its from position
            // this pipe is at the "to" position of the "other".
            if ( pos == "From") AddVertex(G,other,pipe);

        }

        counter++;
    }
    cout<< counter << " lines of data read in " << (clock() - begin) / static_cast<double>(CLOCKS_PER_SEC) << " seconds\n";
    cout<< G.size() << " root elements found in pass " << readtype << "\n";

    CreateGraphFromCSV(G,file, --readtype);

}

string getStrId(const Vertex& v)
{
    string s( v.tag );
    s += "_";
    s += v.id.substr(v.id.size()-4);

    return s;
}

void PrintGraphEdgeList(const Graph& G){
    for(auto& p : G){
        for(auto& v : p.second)
            cout << p.first.id << "," << p.first.tag << "," << v.id << "," << v.tag << endl;
            //cout<< getStrId(p.first) << ";" << getStrId(v) << endl;
    }
}
void PrintGraphSpreadsheet(const Graph& G){
    cout << "Id\tLabel\tIsPipe\n";
    for(auto& p : G){
        cout<< p.first.id << "\t" << p.first.tag;
        if ( p.first.is_pipe && p.first.type != "Connector" ) cout << "\tTrue\n";
        else cout << "\tFalse\n";
    }
    cout << "\n\nSource\tTarget\tType\n";
    for(auto& p : G){
        for(auto& v : p.second)
            cout << p.first.id << "\t" << v.id << "\tDirected\n";
    }


}
// gets the out degree of a root node
int ListSize(const AdjacencyList& L)
{
    int counter = 0;
    for(const auto& a: L) counter++;
    return counter;
}

void cutPipeLoops(Graph& G)
{
   unordered_map<string,pair<int,int>> degrees;
   for(auto& p : G){
        const Vertex& root = p.first;
        AdjacencyList& L = p.second;
        for(auto v: L)
        {
            degrees[root.id].second++;
            degrees[v.id].first++;
        }
   }
   vector<Vertex> to_removeG;
   for(auto& p : G){
        AdjacencyList& L = p.second;
        if ( ListSize(L) > 1 )
        {
            vector<Vertex> to_removeL;
            for(auto v: L)
            {

                pair<int,int> inoutdeg = degrees[v.id];
                if ( inoutdeg.first == 1 && inoutdeg.second == 1)
                {
                    AdjacencyList& adgv = G[v];
                    auto iter = find(L.before_begin(),L.end(),adgv.front());
                    if ( iter != L.end() )
                    {
                        to_removeL.push_back(v);
                        to_removeG.push_back(v);
                    }
                }
            }
            for(auto v : to_removeL) L.remove(v);
        }
    }
    for(auto v : to_removeG) G.erase(v);
}

bool GetSubgraph(   const Vertex& u,
                    const Vertex& target,
                    const Graph& G,
                    Graph& H,
                    const forward_list<string>& drawing_wl,
                    //const forward_list<string>& connector_wl,
                    deque<Vertex> stack = deque<Vertex>())
{
    if (u == target) return true;

    static bool first = true;

    if ( u.is_pipe &&
        find( drawing_wl.begin(), drawing_wl.end(), u.dwg ) == drawing_wl.end() ) return false;

    //    if ( u.type == "Connector" &&
    //        find( connector_wl.begin(), connector_wl.end(), u.tag ) == connector_wl.end() ) return false;

    if (u.tag.substr(0,2) == "TQ" && !first )
    {
        return false;
    }

    first = false;

    if ( u.type == "Secondary Piping") return false;

    stack.push_front(u);
    bool is_path = false;

    for( auto& v : G.at(u))
    {
        if ( find( stack.begin(), stack.end(), v) == stack.end() &&
        //GetSubgraph(v,target,G,H,drawing_wl,connector_wl,stack) )
        GetSubgraph(v,target,G,H,drawing_wl,stack) )
        {
            AddRootVertex(H,u);
            AddRootVertex(H,v);
            AddVertex(H,u,v);
            //AddVertex(H,v,u);
            is_path = true;
        }

    }
    stack.pop_front();
    return is_path;
}



bool ProcessInput(const Graph& G){
    cout << ">";
    string line;
    getline(cin,line);
    stringstream s(line);
    string command;
    getline(s, command, ' ');


    if (line == "") return true;
    if (command=="q") return false;
    if (command=="h") {cout<< usage; return true;}

    if(command=="f"){

        string id;
        getline(s, id, ' ');

        Vertex v;
        v.id = id;
        auto it = G.find(v);
        if ( it != G.end()){
            for(auto& a : it->second)
            {
                cout << a.id << "\t" << a.tag << "\t" << a.dwg
                << "\t" << a.type << "\t" << endl;
            }
        }
        else{
            cout << "Id not found: " << id << endl;
        }
        return true;
    }
    if (command=="p"){

        Vertex start, target;
        getline(s, start.id, ' ');
        getline(s, target.id, ' ');

        string data;
        forward_list<string> dwg_wl; // drawing white list
        getline(s, data, ' ');
        while (data != "")
        {
            dwg_wl.push_front(data);
            data = "";
            getline(s, data, ' ');
        }

//        forward_list<string> connector_wl; // connector black list
//        getline(s, data, ' ');
//        while (data != "q")
//        {
//            connector_wl.push_front(data);
//            getline(s, data, ' ');
//        }

        // sanity check
        Graph::const_iterator sit, tit;
        if ( (sit = G.find(start)) == G.end() ) {cout << "Start vertex not found.\n";return true;}
        if ( (tit = G.find(target)) == G.end() ){cout << "Target vertex not found.\n";return true;}
        //const Vertex& x = sit->first;
        if ( sit->first.is_pipe && find(dwg_wl.begin(),dwg_wl.end(), sit->first.dwg) == dwg_wl.end()) {cout << "Start iten dwg not in allowed list.\n";return true;}
        if ( tit->first.is_pipe && find(dwg_wl.begin(),dwg_wl.end(), tit->first.dwg) == dwg_wl.end()) {cout << "Target iten dwg not in allowed list.\n";return true;}


        Graph H;
        auto begin = clock();
        //GetSubgraph(sit->first,tit->first,G,H, dwg_wl,connector_wl);
        GetSubgraph(sit->first,tit->first,G,H, dwg_wl);
        cutPipeLoops(H);
        PrintGraphSpreadsheet(H);
        cout<< "Command completed in " << (clock() - begin) / static_cast<double>(CLOCKS_PER_SEC) << " seconds\n";
        return true;
    }
    return true;
}



int main(int argc, char* argv[])
{
    if (argc < 2){
        cout << usage;
        return 0;
    }

    ifstream file(argv[1]);
    if ( !file.is_open() ){
        cout<< "File not found:" << argv[1] << endl;
        return 0;
    }

    Graph G;
    CreateGraphFromCSV(G,file,3);
    //PrintGraph(G);

    string op;
    while( ProcessInput(G) );

    return 0;

}

// p C558A0627C9446548B23254872701164 7E4CDFE4292B4A6C98287BF7C126B689 I-DE-3010.1M-5241-944-P4X-002 I-DE-3010.1M-5241-944-P4X-003 I-DE-3010.1M-5111-944-P4X-004
























