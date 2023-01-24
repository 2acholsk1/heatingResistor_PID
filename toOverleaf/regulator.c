struct PID
{
	float U;
	float Kp;
	float Ki;
	float Kd;
	float error;
	float previousError;
	float previousIn;
	float UP, UD, UI;
	float Tp;
};

struct PID pid;


void calcPID(float desiredTemperature, float currentTemperature,
                                         struct PID *PID)
{

	PID->error = desiredTemperature - currentTemperature;

	PID->UP = PID->Kp * PID->error;
	PID->UI = PID->Ki * PID->Tp / 2.0 * 
                (PID->error + PID->previousError) + PID->previousIn;
	PID->UD = PID-> Kd *(PID->error - PID->previousError) / PID->Tp;

	PID->previousError = PID->error;
	PID->previousIn = PID->UI;

	PID->U = PID->UP + PID->UI + PID->UD;

}
