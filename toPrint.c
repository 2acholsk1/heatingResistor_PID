void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim)
{
	if(htim->Instance == TIM3)
	{
		BMP280_ReadTemperatureAndPressure(&temperature_f, 
                                                &pressure);

		__HAL_TIM_SET_COMPARE(&htim1, TIM_CHANNEL_1, pulseOut);


		if(refTemp < 20.0)
			{
			refTemp = 20.0;
			}
		else if(refTemp > 40.0)
			{
			refTemp = 40.0;
			}

		calcPID(refTemp, temperature_f, &pid);

		pulse = htim1.Init.Period * pid.U;

		if(pulse < 0.0)
			{
			pulseOut = 0;
			}
		else if(pulse > htim1.Init.Period)
			{
			pulseOut = htim1.Init.Period;
			}
		else
			{
			pulseOut = (uint16_t) pulse;
			}

		sprintf(currentTemperature_ch, "%f : %f \n\r", temperature_f,
                                                             refTemp);
		HAL_UART_Transmit(&huart3, (uint8_t *)currentTemperature_ch, 
								sizeof(currentTemperature_ch)-1, 1000);
		
		HAL_GPIO_TogglePin(LED_BLUE_GPIO_Port, LED_BLUE_Pin);
	}
}
