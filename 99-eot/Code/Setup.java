import java.util.ArrayList;
public class Setup
{
  /*
  ** This example is based on the model published in the New York Times Article
  ** "How Game Theory Helped Improve New York City’s High School Application Process"
  ** Author: Tracy Tullis  Date: Dec. 5, 2014
  ** https://www.nytimes.com/2014/12/07/nyregion/how-game-theory-helped-improve-new-york-city-high-school-application-process.html
  */


  /* Returns the pre-generated list of Students who have ranked
  ** their preferred schools.
  */
  public static ArrayList<Student> generateStudents()
  {
    //This ArrayList will hold each individual Student Object's ranked schools
    ArrayList<Integer> rankedSchools;

    //Student A
    rankedSchools = new ArrayList<Integer>();
    rankedSchools.add(1);
    rankedSchools.add(2);
    rankedSchools.add(3);
    Student A = new Student("A", rankedSchools);

    //Student B
    rankedSchools = new ArrayList<Integer>();
    rankedSchools.add(2);
    rankedSchools.add(1);
    Student B = new Student("B", rankedSchools);

    //Student C
    rankedSchools = new ArrayList<Integer>();
    rankedSchools.add(1);
    rankedSchools.add(3);
    rankedSchools.add(2);
    Student C = new Student("C", rankedSchools);

    //Student D
    rankedSchools = new ArrayList<Integer>();
    rankedSchools.add(1);
    rankedSchools.add(3);
    rankedSchools.add(2);
    Student D = new Student("D", rankedSchools);

    //Student E
    rankedSchools = new ArrayList<Integer>();
    rankedSchools.add(3);
    rankedSchools.add(2);
    rankedSchools.add(1);
    Student E = new Student("E", rankedSchools);

    //Student F
    rankedSchools = new ArrayList<Integer>();
    rankedSchools.add(1);
    rankedSchools.add(2);
    Student F = new Student("F", rankedSchools);

    //Student G
    rankedSchools = new ArrayList<Integer>();
    rankedSchools.add(1);
    rankedSchools.add(3);
    rankedSchools.add(2);
    Student G = new Student("G", rankedSchools);

    //Student H
    rankedSchools = new ArrayList<Integer>();
    rankedSchools.add(3);
    rankedSchools.add(2);
    Student H = new Student("H", rankedSchools);

    //Student I
    rankedSchools = new ArrayList<Integer>();
    rankedSchools.add(1);
    rankedSchools.add(2);
    rankedSchools.add(3);
    Student I = new Student("I", rankedSchools);

    //Student J
    rankedSchools = new ArrayList<Integer>();
    rankedSchools.add(2);
    rankedSchools.add(1);
    rankedSchools.add(3);
    Student J = new Student("J", rankedSchools);

    //Add Students to the ArrayList
    ArrayList<Student> students = new ArrayList<Student>();
    students.add(A);
    students.add(B);
    students.add(C);
    students.add(D);
    students.add(E);
    students.add(F);
    students.add(G);
    students.add(H);
    students.add(I);
    students.add(J);

    return students;
  }//end generateStudents

  /* Returns the pre-generated list of Schools who have ranked
  ** their preferred students.
  ** Note: Each school ranked 4 students BUT can only accept 3
  */
  public static ArrayList<School> generateSchools()
  {
    //This ArrayList will hold each individual School Object's ranked students
    ArrayList<String> rankedStudents;

    //School 1
    rankedStudents = new ArrayList<String>();
    rankedStudents.add("A");
    rankedStudents.add("B");
    rankedStudents.add("C");
    rankedStudents.add("D");
    School s1 = new School(1, rankedStudents);

    //School 2
    rankedStudents = new ArrayList<String>();
    rankedStudents.add("E");
    rankedStudents.add("F");
    rankedStudents.add("G");
    rankedStudents.add("D");
    School s2 = new School(2, rankedStudents);

    //School 3
    rankedStudents = new ArrayList<String>();
    rankedStudents.add("A");
    rankedStudents.add("D");
    rankedStudents.add("H");
    rankedStudents.add("I");
    School s3 = new School(3, rankedStudents);

    //Add Schools to the ArrayList
    ArrayList<School> schools = new ArrayList<School>();
    schools.add(s1);
    schools.add(s2);
    schools.add(s3);

    return schools;
  }//end generateSchools
}//end class
