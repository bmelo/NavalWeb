#include <iostream>
#include <memory>
#include <unordered_map>
#include <chrono>
#include <forward_list>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <deque>

using namespace std;

struct Vertex{
    //Vertex(bool _isPipe = false):is_pipe(_isPipe){}
    string id;
    string tag;
    string dwg;
    //bool is_pipe = false;
    bool operator==(const Vertex& rhs) const {return this->id == rhs.id;}
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
    <id> : lists adjacency list of of element <id>\n\
    q    : quit\n";

void AddVertex(Graph& G, const Vertex& u, const Vertex& v){

    auto it = G.find(u);

    // if the ID is not yet in the Graph as a root element
    // insert it as a root in the list
    if( it == G.end() ){
        AdjacencyList L;
        L.push_front(v);
        G.insert( pair<Vertex,AdjacencyList>(u,L) );
    }
    else
    {
        AdjacencyList& L = it->second;
        if ( find( L.begin(),L.end(), v ) == L.end() )
            it->second.push_front(v);
    }

}

void CreateGraphFromCSV(Graph& G, ifstream& file)
{
    auto begin = clock();
    string line;
    int counter = 0;
    getline(file,line);
    while ( getline(file,line))
    {
        if (line =="") continue;
        stringstream ss(line);
        string crap;
        string dwg;
        Vertex pipe;
        Vertex other;

        getline(ss, pipe.tag, ';');
        getline(ss, pipe.id, ';');
        getline(ss, crap, ';');
        getline(ss, dwg, ';');
        getline(ss, other.tag, ';');
        getline(ss, other.id, ';');
        other.dwg = pipe.dwg = dwg;

        AddVertex(G,pipe,other);
        AddVertex(G,other,pipe);

        counter++;
    }
    cout<< counter << " lines of data read in " << (clock() - begin) / static_cast<double>(CLOCKS_PER_SEC) << " seconds\n";
    cout<< G.size() << " root elements found.\n";
}
void PrintGraph(const Graph& G){
    for(auto& p : G){
        cout << p.first.id << " - ";
        for(auto& v : p.second)
            cout << v.id << " ";
        cout << endl;
    }
}

bool GetSubgraph(const Vertex& u, const Vertex& target, const Graph& G, Graph& H,const forward_list<string>& whitelist, deque<Vertex> stack = deque<Vertex>())
{
    if (u == target) return true;
    if ( find( whitelist.begin(), whitelist.end(), u.dwg ) == whitelist.end() ) return false;

    stack.push_front(u);
    bool is_path = false;
    for( auto& v : G.at(u))
    {
        if ( find( stack.begin(), stack.end(), v) == stack.end() && GetSubgraph(v,target,G,H,whitelist,stack) )
        {
            AddVertex(H,u,v);
            AddVertex(H,v,u);
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

    if(command=="f"){

        string id;
        getline(s, id, ' ');

        Vertex v;
        v.id = id;
        auto it = G.find(v);
        if ( it != G.end()){
            for(auto& a : it->second)
            {
                cout << a.id << "\t" << a.tag << endl;
            }
        }
        else{
            cout << "Id not found: " << id << endl;
        }
        return true;
    }
    if (command=="p"){
        Graph H;
        Vertex start, target;
        getline(s, start.id, ' ');
        getline(s, start.dwg, ' ');
        getline(s, target.id, ' ');

        string data;
        forward_list<string> whitelist;
        cout<<"Enter allowed drawings list, q to finish.\n";
        while (data != "q")
        {
            cout<< ">";
            cin>> data;
            if ( data != "q" ) whitelist.push_front(data);
        }
        auto begin = clock();
        GetSubgraph(start,target,G,H, whitelist);
        PrintGraph(H);
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
    CreateGraphFromCSV(G,file);
    //PrintGraph(G);

    string op;
    while( ProcessInput(G) );

    return 0;

}
























