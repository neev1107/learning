import java.util.Scanner;
class Firatclass{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("PLease enter Temperature: ");
        int Temp = sc.nextInt();
        System.out.print("Please enter units: ");
        String unit = sc.next();
        if(Temp <0) {
            System.out.print("Freezing");
        } else if(0 <= Temp && Temp<=10) {
            System.out.print("Extreme cold");
        } else if(11<=Temp && Temp<=20) {
            System.out.print("Ver Cold");
        } else if(21<=Temp && Temp<=30) {
            System.out.print("Warm");
        } else {
            System.out.print("You get burn");
        }
    }
}