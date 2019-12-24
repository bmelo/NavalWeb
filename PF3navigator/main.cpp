#include <iostream>
#include <memory>
#include <unordered_map>
#include <chrono>
#include <forward_list>
#include <sstream>
#include <fstream>

using namespace std;

struct Node{
    Node(bool _isPipe = false):is_pipe(_isPipe){}
    string id;
    string tag;
    bool is_pipe = false;
    bool visited = false;
    shared_ptr<Node> next;
    bool operator==(const Node& rhs) const {return this->id == rhs.id;}
};
struct hash_node{
    size_t operator()(const Node& N) const{
        hash<string> hstr;
        return hstr(N.id);
    }
};
using AdjList = forward_list<Node>;
using Graph = unordered_map<Node,AdjList,hash_node>;

const char * usage = "\
PF3 - read and navigate through PF3 data\n\
usage: PF3 <file name>\n\
commands:\n\
    <id> : lists adjacency list of of element <id>\n\
    q    : quit\n";

void insert_node(Graph& G, Node& U, Node& V){

    auto it = G.find(U);

    // if the element is not yet in the map as a root element
    // insert it as a root in the list
    if( it == G.end() ){
        AdjList L;
        L.push_front(V);
        G.insert( pair<Node,AdjList>(U,L) );
    }
    else
    {
        it->second.push_front(V);
    }

}

void read_graph(Graph& G, ifstream& file)
{
    auto begin = clock();
    string line;
    int counter = 0;
    getline(file,line);
    while ( getline(file,line))
    {
        stringstream ss(line);
        string crap;
        Node P(true);
        Node O;

        getline(ss, P.tag, ';');
        getline(ss, P.id, ';');
        getline(ss, crap, ';');
        getline(ss, crap, ';');
        getline(ss, O.tag, ';');
        getline(ss, O.id, ';');

        insert_node(G,P,O);
        insert_node(G,O,P);

        counter++;
    }
    cout<< counter << " lines of data read in " << (clock() - begin) / static_cast<double>(CLOCKS_PER_SEC) << " seconds\n";
    cout<< G.size() << " root elements found.\n";
}

bool process_input(const Graph& G){
    cout << ">";
    string data;
    getline(cin,data);

    if (data == "") return true;

    if (data=="q") return false;
    else{
        Node n;
        n.id = data;
        auto it = G.find(n);
        if ( it != G.end()){
            for(auto& a : it->second)
            {
                cout << a.id << "\t" << a.tag << endl;
            }
        }
        else{
            cout << "Id not found: " << data << endl;
        }
        return true;
    }
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
    read_graph(G,file);

    string op;
    while( process_input(G) );

    return 0;

}
























