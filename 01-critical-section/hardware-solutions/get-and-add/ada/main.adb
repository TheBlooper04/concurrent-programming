with Ada.Text_IO; use Ada.Text_IO;
with System.Atomic_Operations; use System.Atomic_Operations;
with System.Atomic_Operations.Integer_Arithmetic;

procedure Main is
   Max_Value   :  constant Integer := 1_000_000;
   Num_Threads :  constant Integer := 10;
   Iterations  :  constant Integer := Max_Value / Num_Threads; 

   type Atomic_Integer is new Integer with Atomic;
   package Atomic_Ops is new Integer_Arithmetic (Atomic_Integer);
   
   Counter : aliased Atomic_Integer := 0;
   Added_Value : constant Atomic_Integer := 1;

   task type Worker is
      entry Start(Idx : Integer);
   end Worker;

   task body Worker is
      Tid : Integer;
   begin
      accept Start(Idx: Integer) do
         Tid := Idx;
      end Start;

      for I in 1 .. Iterations loop
         Put_Line("Thread " & Tid'Image & ": adding 1 to the counter value.");
         Atomic_Ops.Atomic_Add (Counter, Added_Value);
      end loop;
   end Worker;

   type Tasks is array (1 .. Num_Threads) of Worker;

begin
   declare
      Workers : Tasks;
   begin
      for I in 1 .. Num_Threads loop
         Workers (I).Start (I);
      end loop;
   end; 

   Put_Line("Counter value: " & Counter'Image & " | Expected value: " & Max_Value'Image);
end Main;

