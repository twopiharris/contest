// BizBaz.cpp
//C++ version of BizBaz

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

using namespace std;

int primes[] =       {2,     3,     5,      7,    11,     13};
string terms[] = {"Biz ", "Baz ", "Buzz ", "Boz ", "Beez ", "Bizzle "};

int main(){
    ifstream inFile;
    ofstream outFile;
    inFile.open("bizBazIn.txt");
    outFile.open("bizBazOut.txt");
    int attack;
    while(!inFile.eof()){
        inFile >> attack;
        bool hit = true;
        outFile << attack << " ";
        cout << attack << " ";
        for (int i = 0; i < 6; i++){
            int prime = primes[i];
            if (attack % prime == 0){
                hit = false;
                outFile << terms[i];
                cout << terms[i];
            } // end if
        } // end for
        if (hit){
           outFile << "Bummer";
           cout << "Bummer";
        } // end if
        
        outFile << endl;
        cout << endl;
        
    } // end while
    inFile.close();
    outFile.close();
} // end main