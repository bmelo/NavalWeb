#include <iostream>
#include <fstream>
#include <sstream>
#include <forward_list>
#include <ctime>
#include <cstddef>

using namespace std;

struct data_line
{
    string tag_pipe;
    string tag_other;
    string dwg;
    string pos;
    string type;
    string pipe_id;
    string other_id;
};
ostream & operator<<(ostream & os, const data_line & d)
{
    os<< d.tag_pipe << "\t" << d.pipe_id << "\t"
      << d.tag_other << "\t" << d.other_id << "\t"
      << d.pos << "\t" << d.dwg << "\t" << d.type;

    return os;
}

void print_data(const forward_list<data_line> & list, size_t offset, string data)
{
    int line = 2;
    for(auto it = list.cbegin(); it != list.end(); it++ )
    {
        char * base = (char*)(&(*it));
        string * ptr = (string *) (base+offset);

        if ( (*ptr) == data )
           cout << line << "\t" << (*it) << endl;
        line++;
    }
}
void print_line(const forward_list<data_line> & list, string data)
{
    int line_num = atoi(data.c_str());
    auto it = list.cbegin();
    for(int i = 2; i<line_num;i++) it++;
    cout << line_num << "\t" << (*it) << endl;
}

void print_dwg(const forward_list<data_line> & list, string data)
{
    int line = 2;
    int found = 0;
    for(const auto& d: list ){
        if( d.dwg == data ) {
            cout << line << "\t" << d << endl;
            found++;
        }
        line++;
    }
    cout << found << " occurences found.\n";
}

const char * usage = "\
PF3 - read and navigate through PF3 data\n\
usage: PF3 <file name>\n\
commands:\n\
    p <tag> : lists occurences of tag_pipe = <tag>\n\
    o <tag> : lists occurences of tag_other = <tag>\n\
    pi <id> : lists occurences of pipe id  = <id>\n\
    oi <id> : lists occurences of other id = <id>\n\
    l <line>: lists contents of line <line>\n\
    d <dwg> : lists lines where drawing = <dwg>\n\
    h       : print this help.\n\
    q       : quit\n";


int main(int argc, char * argv[]){
    if (argc < 2){
        cout << usage;
        return 0;
    }

    ifstream file(argv[1]);
    if ( !file.is_open() ){
        cout<< "File not found:" << argv[1] << endl;
        return 0;
    }

    forward_list<data_line> list;

    // gets the 1st line, header
    string line;
    getline(file,line);
    cout << "Reading data from" << argv[1] << ". Please wait...\n";
    int counter = 0;
    auto begin = clock();

    while ( getline(file,line))
    {
        // used for breaking words
        stringstream s(line);
        string crap;
        data_line d;

        getline(s, d.tag_pipe, ';');
        getline(s, d.pipe_id, ';');
        getline(s, crap, ';');
        getline(s, d.dwg, ';');
        getline(s, d.tag_other, ';');
        getline(s, d.other_id, ';');
        getline(s, d.pos, ';');
        getline(s, d.type, ';');

        list.push_front(d);
        counter++;
    }
    list.reverse();
    cout<< counter << " lines of data read in " << (clock() - begin) / static_cast<double>(CLOCKS_PER_SEC) << " seconds\n";
    string op;
    do{
        cout << ">";
        getline(cin,line);
        stringstream s(line);      
        getline(s, op, ' ');

        string data;
        getline(s, data);

        if ( op=="p"  ) {print_data(list, offsetof(data_line, tag_pipe), data ); continue;}
        if ( op=="o"  ) {print_data(list, offsetof(data_line, tag_other), data );continue;}
        if ( op=="pi" ) {print_data(list, offsetof(data_line, pipe_id), data );continue;}
        if ( op=="oi" ) {print_data(list, offsetof(data_line, other_id), data );continue;}
        if (op=="d") print_dwg(list,data);
        if (op=="l") print_line(list,data);
        if (op=="h") cout << endl << usage << endl;

    }while(op != "q");


    return 0;
}
