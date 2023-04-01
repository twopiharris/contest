#include <iostream>
#include <fstream>

using namespace std;

unsigned long calcFib(int limit){
    unsigned long a = 1;
    unsigned long b = 1;
    unsigned long sum = 0;
    for (int i = 0; i < limit -2; i++){
        sum = a + b;
        a = b;
        b = sum;
    } // end for
    return(sum);
} // end calcFib

int main(){
    ifstream inFile;
    inFile.open("bigFibIn.txt");
    int limit;
    
    while(!inFile.eof()){
        inFile >> limit;
        cout << calcFib(limit) << endl;
    } // end while

    return(0);
} // end main