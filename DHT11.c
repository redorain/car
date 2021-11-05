#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <wiringPi.h>

typedef unsigned long uint32;
typedef unsigned int  uint16;
typedef unsigned char uint8;

uint32 databuff;/*Define a variable to store the 32 bit
                 * temperature and humidity data measured by sensor DHT11*/

/*By calling this function(void Init_GPIO(int gpio_pin)),the initial state
 * of the data pin of the host connected to the sensor has been set to high
 * level and keep this high level output steady for at least 1 second*/
void Init_GPIO(int gpio_pin)
{
    pinMode(gpio_pin,OUTPUT); //Set pin to output mode //Initialize pin

    digitalWrite(gpio_pin,1); //Output a high level on that pin
    sleep(1); //Let the high level on that pin lasts for 1ms(1000us)
    /*No operation will be done during the first 1 second after the sensor is
     * powered-on,in order to keep the level output by the pin of the host to
     * the data line as well as the sensor stable*/
}


/*By calling this function(void Start_DHT11(int gpio_pin)),The host sends an
 * start signal to the sensor to activate(start) the sensor*/
void Start_DHT11(int gpio_pin)
{
    pinMode(gpio_pin, OUTPUT); //Set pin to output mode
    digitalWrite(gpio_pin, 0); //Output a low level on that pin
    delay(25);
    /*The host pulls down the output level to low level on data pin after 1s's
     * high level and keep this low level for a while by set its delay to 25us
     * in order to begin to send a start signal to sensor*/

    digitalWrite(gpio_pin,1); //Output a high level on that pin
    pinMode(gpio_pin,INPUT);//Set pin to input mode
    pullUpDnControl(gpio_pin,PUD_UP); /*While the pin has been set to input mode,
                                       * use this function pullUpDnControl to
                                       * activate its inner pull-up resistor
                                       * or pull-down resistor*/
    delayMicroseconds(30);
    /*The host then pulls up the output level to high level on data pin after
     * 25us'low level and keep this high level for a while by set its delay to
     * 30us in order to finish the
     * transmission of start signal to start and wait for sensor DHT11 to response*/
}

/*By calling this function(uint8 Read_DHT11(int gpio_pin)),the host begin to
 * receive 40 bit data measured and sent by sensor DHT11*/
uint8 Read_DHT11(int gpio_pin)
{
    uint8 i;
    /*By doing this if statement the host begin to receive 32 bit
     * temperature and humidity data measured and sent by sensor DHT11*/
    if (0 == digitalRead(gpio_pin))	/*Judge if the host receive the former part
                                     * (low level)of the respond signal sent by
                                     * sensor DHT11*/
    {
        while(!digitalRead(gpio_pin));/*Judge if the host receive the latter part
                                       * (high level) of the respond signal sent by
                                       * sensor DHT11*/

        /*By doing this for statement the host begin to receive 32 bit temperature
         * and humidity data measured by sensor DHT11 bit by bit*/
        for (i = 0; i < 32; i++)
        {
            while(digitalRead(gpio_pin));	/*Judge if the host receive a new data
                                             * bit sent by sensor DHT11 by detect
                                             * the 55us' low level at the beginning
                                             * of the transmission of a data bit*/
            while(!digitalRead(gpio_pin));	/*Begin to judge if the value of data bit
                                             * sent by sensor DHT11 is logic"0" or
                                             * logic"1"by detect its level output
                                             * is logic"0" or logic"1" after the 55us'
                                             * low level at the beginning of the
                                             * transmission of a data bit*/

            delayMicroseconds(36);/*Make a 36us' delay which is long enough to identify
                                   * the data bit sent by sensor DHT11 is whether
                                   * logic"0" or logic"1"*/

            databuff *= 2;/*Left shift the data bit received from sensor DHT11 this time
                           * which is stored in variable databuff in order get prepared
                           * to read next data bit from sensor */

            if (digitalRead(gpio_pin) == 1)/*Judge if the value of the data bit sent by
                                            * sensor DHT11 is a logic"1" or logic"0" by
                                            * detect the level output after 36 us'
                                            * delay is high level or low level*/
            {
                databuff++;/*Store a logic value"1" into variable databuff if the
                            * level output after 36 us' delay is high level*/
                           /*Else a logic"0" is stored into variable databuff if the
                            * level output after 36 us' delay is low level*/
            }
        }

        /*By doing this for statement the host begin to receive 8 bit parity data
         * calculated by sensor DHT11 bit by bit*/
        uint8 crc;/*Define a variable to store the 8 bit parity data calculated
                   * by sensor DHT11*/
        for (i = 0; i < 8; i++)
        {
            while (digitalRead(gpio_pin));/*Judge if the host receive a new parity
                                           * bit sent by sensor DHT11 by detect the
                                           * 55us' low level at the beginning of the
                                           * transmission of a data bit*/
            while (!digitalRead(gpio_pin));/*Begin to judge if the value of parity
                                            * bit sent by sensor DHT11 is logic"0"
                                            * or logic"1"by detect its level output
                                            * is logic"0" or logic"1" after the 55us'
                                            * low level at the beginning of the
                                            * transmission of a data bit*/

            delayMicroseconds(36);/*Make a 36us' delay which is long enough to identify
                                   * the parity bit sent by sensor DHT11 is whether
                                   * logic"0" or logic"1"*/

            crc *= 2;/*Left shift the parity bit received from sensor DHT11 this time
                      * which is stored in variable crc in order get prepared to read next
                      * parity bit from sensor */
            if (digitalRead(gpio_pin) == 1)/*Judge if the value of the parity bit sent
                                            * by sensor DHT11 is a logic"1" or logic"0"
                                            * by detect the level output after 36 us'
                                            * delay is high level or low level*/
            {
                crc++;/*Store a logic value"1" into variable crc if the level output
                       * after 36 us' delay is high level*/
                      /*Else a logic"0" is stored into variable crc if the
                       * level output after 36 us' delay is low level*/
            }
        }
        return 1;
    }
    else
    {
        return 0;
    }
}

int main(int argc, char *argv[])
{
    if (2 != argc) /*Check if the number of the arguements input to call this program
                    * is right(equal 2)*/
    {
        printf("The format of the arguments to call this program is: %s gpio_pin\n", argv[0]);
        /*If the number of the arguements input less or more 2,hint user the correct format
         * calling this program*/
        return 0;
    }

    if (wiringPiSetup() == -1) //Check if the wiringPi library is configured correctly
    {
        printf("Failed to setup WiringPi!\n"); /*Report the error detected in
                                                * setting up wiringPi to user if the
                                                * wiringPi library is configured incorrectly*/
        return 1;
    }

    while(1)
    {
        Init_GPIO(atoi(argv[1]));/*Call the function(Init_GPIO(atoi(argv[1]))) to initial
                                  * the pin of the host connected to sensor DHT11*/

        Start_DHT11(atoi(argv[1]));/*Call the function(Start_DHT11(atoi(argv[1]))) to
                                    * activate(start) the sensor DHT11*/

        if (Read_DHT11(atoi(argv[1])))/*Call the function(Read_DHT11(atoi(argv[1]))) to
                                       * receive data measured by sensor DHT11 bit by bit*/
        {
            printf("RH:%d.%d\n", (databuff >> 24) & 0xff, (databuff >> 16) & 0xff);
            /*Take out the integer and fractional part of temperature data from the
             * variable databuff which store 40bit data in total,convert the temperature
             * data from binary form to decimal form and display it on screen
             * connected to host*/

            printf("TMP:%d.%d\n", (databuff >> 8) & 0xff, databuff & 0xff);
            /*Take out the integer and fractional part of humidity data from the variable
             * databuff which store 40bit data in total,convert the humidity data from
             * binary form to decimal form and display it on screen connected to host*/

            databuff = 0;
            //Clear the variable databuff for receiving the data measured next time
        }
        else
        {
            printf("Sensor dosent ans!\n");
            databuff = 0;
        }

        sleep(3);
    }

    return 0;
}
//
// Created by 18355 on 2021/10/23.
//

