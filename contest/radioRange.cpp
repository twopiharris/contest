//radioRange.cpp

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cmath>

using namespace std;

int main(){
    ifstream inFile;
    ofstream outFile;
    inFile.open("radioRangeIn.txt");
    outFile.open("radioRangeOut.txt");
    int x1, y1, r1, x2, y2, r2;
    
    while(!inFile.eof()){
        inFile >> x1;
        inFile >> y1;
        inFile >> r1;
        inFile >> x2;
        inFile >> y2;
        inFile >> r2;
        int dist = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
        outFile << dist << endl;
    } // end while

    inFile.close();
    outFile.close();
}