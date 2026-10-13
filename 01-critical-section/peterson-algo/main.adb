with Ada.Text_IO; use Ada.Text_IO;

procedure Main is
   Max_Value   : constant := 1_000_000;
   Num_Threads : constant := 2;

   type Binary_Integer is new Integer range 0 .. 1;
   type Boolean_Array is array (0 .. Num_Threads - 1) of Binary_Integer;

   Want_Cs  : Boolean_Array   := (0, 0);
   Turn     : Integer         := 0;
   Counter  : Integer := 0;

   task type Worker is
      entry Start(Idx : Integer);
   end Worker;

   task body Worker is
      Tid : Integer;
      Other_Tid : Integer;
   begin
      accept Start(Idx : Integer) do
         Tid := Idx;
      end Start;

      for I in 1 .. (Max_Value / Num_Threads) loop
         Want_Cs(Tid) := 1;
         Other_Tid := (Tid + 1) mod Num_Threads;
         Turn := Other_Tid;
         while Want_Cs(Other_Tid) = 1 and Turn = Other_Tid loop
            null;
         end loop;
         
         Put_Line("Thread " & Tid'Image & ": adding 1 to the counter value.");
         Counter := Counter + 1;

         Want_Cs(Tid) := 0;
      end loop;
   end Worker;

   type Tasks is array (0 .. Num_Threads - 1) of Worker;

begin
   declare 
      Workers : Tasks;
   begin
      for I in 0 .. Num_Threads - 1 loop
         Workers (I).Start (I);
      end loop;
   end;

   Put_Line("Counter value:" & Counter'Image & " | Expected value: " & Max_Value'Image);
end Main;