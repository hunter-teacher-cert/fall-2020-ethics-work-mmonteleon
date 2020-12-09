import java.util.ArrayList;
public class Student
{
    private String name;
    private ArrayList<Integer> rankedSchools = new ArrayList<Integer>();
    private int school;

    public Student(String name, ArrayList<Integer> rankedSchools)
    {
        this.name = name;
        this.rankedSchools = rankedSchools;
        this.school = -1;  //Default to no school
    }

    public String getStudentName()
    {
      return name;
    }

    /*
    ** Students can only be ranked IF
    ** They have schools left in their list that they were not yet rejected from.
    ** AND they are not yet matched.
    */
    public boolean canBeRanked()
    {
      return rankedSchools.size() > 0 && school == -1;
    }

    public int topChoice()
    {
      return rankedSchools.remove(0);
    }

    public void setSchool(int school)
    {
      this.school = school;
    }

    public String toString()
    {
      return name + " school: " + school;
    }

    /* Prints the list of Schools ranked by the Student. */
    public void printRankedChoices()
    {
      System.out.print(this.name);
      for(Integer school: rankedSchools)
      {
        System.out.print(" " + school);
      }
      System.out.println();
    }

}
