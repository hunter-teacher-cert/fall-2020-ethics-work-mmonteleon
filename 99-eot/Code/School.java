import java.util.ArrayList;
public class School
{
    private int schoolID;
    private ArrayList<String> rankedStudents; //This is the schools ranking of students
    private ArrayList<Student> matchedStudents;  //students who have received a seat
    private ArrayList<Student> studentPool;  //pool of students who want to be placed

    public School(int schoolID, ArrayList<String> rankedStudents)
    {
        this.schoolID = schoolID;
        this.rankedStudents = rankedStudents;
        this.matchedStudents = new ArrayList<Student>();
        this.studentPool = new ArrayList<Student>();
    }

    // Add a student to the pool of students who want to be placed
    public void addToPool(Student s)
    {
      studentPool.add(s);
    }

    /* Fill the school's available seats with matching students.
    ** Elgible students added to the matchedStudents ArrayList
    */
    public void fillSchool()
    {
      //Check each student in the Pool to see if they were ranked
      for(Student student: studentPool)
      {
        for(String rankedStudent: rankedStudents)
        {
          if(student.getStudentName().equals(rankedStudent))
          {
            matchedStudents.add(student);
            student.setSchool(schoolID);
          }
        }//end rankedStudent loop
      }//end studentPool loop

      //Empty the studentPool
      this.studentPool = new ArrayList<Student>();

      /* The matchedStudents is capped at 3.
      ** If there are more than 3 students, the lowest ranked becomes unmatched.
      */
      if(matchedStudents.size() > 3)
      {
        //loop backwards
        //The lowest ranked student will be at the end.
        for(int i = rankedStudents.size() - 1; i >=0; i--)
        {
          for(int j = 0; j < matchedStudents.size(); j++)
          {
            //lowest ranked match found
            if(rankedStudents.get(i).equals(matchedStudents.get(j).getStudentName()))
            {
              Student removed = matchedStudents.remove(j);
              removed.setSchool(-1);
              return;
            }
          }// end loop through matchedStudents
        }//end loop of rankedStudents
      }//end matchedStudents >3
    }//end fillSchool

    /* Prints the list of Students ranked by the School. */
    public void printRankedChoices()
    {
      System.out.print(this.schoolID);
      for(String student: rankedStudents)
      {
        System.out.print(" " + student);
      }
      System.out.println();
    }
}
