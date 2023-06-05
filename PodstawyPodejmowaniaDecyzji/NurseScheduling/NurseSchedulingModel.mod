/*********************************************
 * OPL 22.1.1.0 Model
 * Author: Mateusz Bogusz
 * Creation Date: 28 May 2023 at 17:59:10
 ********************************************/
int min_shifts = 11; // Minimum number of shifts 
int max_shifts = 13; // / Maximum number of shifts

int N = 30; // Number of days
range days = 1..N;

int total_nurses = 20; // Number of nurses
range nurses = 1..total_nurses;

int total_laboratory_technicians = 5; // Number of laboratory technicians
range technicians = 1..total_laboratory_technicians;

int total_midwives = 10; // Number of midwives
range midwives = 1..total_midwives;

int min_nurses = 4; // Required minimum number of nurses
int min_midwives = 2;  // Required minimum number of midwives
int min_laboratory_technicians = 1; // Required minumum number of laboratory technicians

// Declared work schedudles
int declared_nurses[days][nurses][1..2] = [[[1, 1], [0, 0], [1, 1], [1, 1], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 0], [1, 1], [0, 1], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 0], [0, 0], [1, 1], [0, 1], [0, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 1], [1, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 0], [1, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 1], [0, 0], [1, 0], [0, 0], [1, 1], [1, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 1], [1, 1], [0, 0], [1, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 0], [0, 1], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 0], [1, 1], [1, 1], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 1], [1, 1], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 0], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 0], [0, 0], [0, 0], [0, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 1], [0, 1], [1, 1], [1, 0], [0, 1], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 0], [0, 1], [1, 0], [1, 1], [1, 1], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 1], [0, 0], [0, 0], [1, 1], [0, 1], [0, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1], [1, 0], [0, 1], [1, 0], [1, 1], [0, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 0], [1, 1], [1, 0], [0, 0], [0, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 0], [0, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 1], [1, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [0, 0], [1, 0], [0, 0], [0, 0], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 0], [1, 1], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 0], [0, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]];
int declared_laboratory_technicians[days][technicians][1..2] = [[[1, 0], [1, 1], [1, 0], [1, 1], [1, 1]], [[0, 0], [1, 0], [0, 0], [1, 1], [1, 1]], [[0, 1], [0, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 0], [1, 0], [0, 1], [1, 0], [1, 1]], [[0, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [0, 0], [0, 0], [0, 0], [1, 0]], [[0, 1], [1, 1], [1, 1], [1, 1], [1, 0]], [[1, 1], [1, 1], [0, 1], [1, 0], [1, 0]], [[0, 0], [1, 1], [0, 1], [1, 1], [1, 1]], [[1, 0], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 0], [0, 0], [1, 1], [0, 0], [0, 0]], [[0, 1], [1, 1], [1, 0], [1, 0], [1, 1]], [[1, 0], [0, 1], [1, 0], [1, 1], [1, 1]], [[0, 1], [1, 0], [0, 0], [0, 1], [1, 1]], [[0, 0], [1, 0], [1, 1], [1, 1], [1, 1]], [[1, 0], [1, 1], [1, 0], [0, 0], [1, 1]], [[0, 0], [0, 1], [1, 1], [1, 1], [1, 1]], [[0, 0], [1, 1], [1, 1], [0, 0], [1, 1]], [[0, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 0], [0, 0], [0, 0], [1, 1], [1, 1]], [[0, 0], [1, 1], [0, 0], [1, 0], [1, 1]], [[0, 1], [0, 0], [1, 1], [1, 1], [1, 1]], [[1, 0], [0, 0], [1, 1], [0, 1], [1, 1]], [[1, 0], [1, 1], [1, 1], [0, 1], [1, 1]], [[1, 0], [0, 0], [0, 1], [0, 0], [1, 1]], [[1, 1], [0, 1], [1, 0], [1, 0], [1, 1]], [[1, 0], [0, 1], [0, 1], [1, 1], [1, 1]], [[0, 0], [1, 1], [1, 1], [1, 1], [1, 1]]];
int declared_midwives[days][midwives][1..2] = [[[1, 0], [0, 0], [1, 1], [0, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [0, 0], [0, 0], [1, 1], [0, 0], [1, 1], [0, 0], [1, 0], [1, 1]], [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [0, 0], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 0], [1, 0], [1, 0], [0, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 1], [1, 1], [0, 1], [0, 1], [1, 1], [0, 1], [1, 1], [1, 1], [1, 1]], [[0, 0], [0, 1], [1, 1], [1, 1], [0, 0], [0, 1], [1, 0], [1, 1], [1, 1], [1, 1]], [[1, 0], [0, 0], [1, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 0], [1, 1], [0, 1], [1, 1], [1, 1], [1, 1], [0, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [1, 0], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 0], [0, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 1], [1, 1], [1, 0], [1, 0], [0, 0], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [0, 0], [1, 1], [1, 1], [1, 0], [1, 0], [0, 0], [0, 1], [1, 1], [1, 1]], [[0, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[1, 1], [0, 1], [1, 0], [1, 1], [0, 0], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 1], [0, 0], [0, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]], [[0, 0], [1, 1], [1, 1], [0, 1], [1, 1], [1, 1], [1, 0], [0, 0], [1, 1], [1, 0]], [[1, 1], [1, 0], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]];

// Declare decision variables
dvar boolean schedule_nurses[days][nurses][1..2];
dvar boolean schedule_laboratory_technicians[days][technicians][1..2];
dvar boolean schedule_midwives[days][midwives][1..2];

// Minimize total amount of employees working
minimize 
	sum(day_index in days, nurse_index in nurses, shift_index in 1..2) schedule_nurses[day_index][nurse_index][shift_index] 
	+ sum(day_index in days, technician_index in technicians, shift_index in 1..2) schedule_laboratory_technicians[day_index][technician_index][shift_index] 
	+ sum(day_index in days, midwife_index in midwives, shift_index in 1..2) schedule_midwives[day_index][midwife_index][shift_index];
	
subject to{
  // Each employee can work only one shift a day
  forall(day_index in days){
    forall(nurse_index in nurses){
      sum(shift_index in 1..2) schedule_nurses[day_index][nurse_index][shift_index] <= 1;
    }
    forall(technician_index in technicians){
      sum(shift_index in 1..2) schedule_nurses[day_index][technician_index][shift_index] <= 1;
    }
    forall(midwife_index in midwives){
      sum(shift_index in 1..2) schedule_nurses[day_index][midwife_index][shift_index] <= 1;
    }      
  }
  
  // Each employee can't take day shift after a night shift
  forall(day_index in 1..N-1){
    forall(nurse_index in nurses){
      schedule_nurses[day_index][nurse_index][2] + schedule_nurses[day_index + 1][nurse_index][1] <= 1;
    }
    forall(technician_index in technicians){
      schedule_laboratory_technicians[day_index][technician_index][2] + schedule_laboratory_technicians[day_index + 1][technician_index][1] <= 1;
    }
    forall(midwife_index in midwives){
      schedule_midwives[day_index][midwife_index][2] + schedule_midwives[day_index + 1][midwife_index][1] <= 1;
    }      
  }
  
  // Each employee must work between minimum and maximum number of shifts
  forall(nurse_index in nurses){
    sum(day_index in days, shift_index in 1..2) schedule_nurses[day_index][nurse_index][shift_index] <= max_shifts;
    sum(day_index in days, shift_index in 1..2) schedule_nurses[day_index][nurse_index][shift_index] >= min_shifts;
  }
  
  forall(technician_index in technicians){
    sum(day_index in days, shift_index in 1..2) schedule_laboratory_technicians[day_index][technician_index][shift_index] <= max_shifts;
    sum(day_index in days, shift_index in 1..2) schedule_laboratory_technicians[day_index][technician_index][shift_index] >= min_shifts;
  }
  
  forall(midwife_index in midwives){
    sum(day_index in days, shift_index in 1..2) schedule_midwives[day_index][midwife_index][shift_index] <= max_shifts;
    sum(day_index in days, shift_index in 1..2) schedule_midwives[day_index][midwife_index][shift_index] >= min_shifts;
  }
  
  // Employee can't be assigned to shift if he requested holiday on certain shift
  forall(day_index in days){
    forall(nurse_index in nurses){
      forall(shift_index in 1..2) {
       	(declared_nurses[day_index][nurse_index][shift_index] == 0)  => (schedule_nurses[day_index][nurse_index][shift_index] != 1); 
      }
   	}   
   	
   	forall(technician_index in technicians){
      forall(shift_index in 1..2) {
       	(declared_laboratory_technicians[day_index][technician_index][shift_index] == 0)  => (schedule_laboratory_technicians[day_index][technician_index][shift_index] != 1); 
      }
   	}  
   	
   	forall(midwife_index in midwives){
      forall(shift_index in 1..2) {
       	(declared_midwives[day_index][midwife_index][shift_index] == 0)  => (schedule_midwives[day_index][midwife_index][shift_index] != 1); 
      }
   	}   	
  }
  
  // Required minimum number of employees on each shift from each profession must be satisfied
  forall(day_index in days){
     forall(shift_index in 1..2){
       sum(nurse_index in nurses) schedule_nurses[day_index][nurse_index][shift_index] >= min_nurses;
       sum(technician_index in technicians) schedule_laboratory_technicians[day_index][technician_index][shift_index] >= min_laboratory_technicians;
       sum(midwife_index in midwives) schedule_midwives[day_index][midwife_index][shift_index] >= min_midwives;
     }
  }
}
