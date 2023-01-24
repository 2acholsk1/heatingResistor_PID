
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
	if (huart->Instance == USART3)
	{
		HAL_GPIO_TogglePin(LED_GREEN_GPIO_Port, LED_GREEN_Pin);


			switch(get_RX[0])
			{
				case 'u':
				{
					refTemp += 0.1;
					break;
				}
				case 'd':
				{
					refTemp -= 0.1;
					break;
				}
			}
		HAL_UART_Receive_IT(&huart3, get_RX, 1);

	}
}