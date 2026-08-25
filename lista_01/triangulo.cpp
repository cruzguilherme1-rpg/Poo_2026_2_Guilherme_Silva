class triangulo {
public:    
   double b, h;
   double calcular_area(){

    return b * h / 2;
   }
 
};

int main (){
   triangulo x;
   x.b = 10;
   x.h = 20;
   cout << x.calcular_area();

}