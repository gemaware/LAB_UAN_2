package co.edu.uan.sad.assignment2.exercise2;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Comparativa equals" );
    }
}
public class A {
    int aField;
    @Override
    public boolean equals(Object o) {
        if(this==o) {
            return true;
        }   
        if(o==null) {
            return false;
        }
        if(!(o instanceof A)) {
            return false;
        }
        A other = (A) o;

		return other.aField == afield; /* lineas adicionadas por geovani Martinez*/

}

}
public class B extends A {
    int bField;
    @Override
    public boolean equals(Object o) {
        if(this==o) {
            return true;
        }
        if(!super.equals(o)) {
            return false;
        }
        if(!(o instanceof B)) {
            return false;
        }
        B other = (B) o;

        return super.equals(o) && bField.equals(other.bField);  /* lineas adicionadas por geovani Martinez*/


}
