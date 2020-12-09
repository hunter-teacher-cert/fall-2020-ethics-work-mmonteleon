import java.util.ArrayList;
public class Match
{
  /*
  **  The match method is an application of the Gale-Shapley Algorithm.
  **  Lloyd Shapley and Alvin Roth recieved a Nobel prize in Economic Sciences for this algorithm.
  **  This is the algorithm that the NYCDOE uses to place students during their HS Matching process.
  */
  public static void match(ArrayList<Student> students, ArrayList<School> schools)
  {
    boolean anotherRound = true;
    int round = 1;

    /* Loop while it is still possible to match students. */
    while(anotherRound)
    {
      System.out.println("\nROUND " + round + "\n");
      //Check each Student's current top choice and place them in the school's pool
      for(Student s: students)
      {
        //Ignore students that are already matched
        if(s.canBeRanked())
        {
          //get top choice
          int schoolID = s.topChoice();
          //place in school pool
          schools.get(schoolID-1).addToPool(s);
        }
      }//end students loop

      /* Place students from the pool into their chosen Schools
      ** IF the schools ranked them high enough */
      for(School s: schools)
        s.fillSchool();

      /* Print out the state of each student at the end of the round.
      **               AND
      ** Check if there are any students left to be ranked.
      */
      anotherRound = false;
      for(Student s: students)
      {
        System.out.println(s);
        if(s.canBeRanked())
          anotherRound = true;
      }
      round++;
    }//end while loop
  }//end match

}
