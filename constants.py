import navx
import math

COMP_BOT =       0
PRACTICE_BOT =   1

ROBO_RIO_PWM_0 = 0
ROBO_RIO_PWM_1 = 1
ROBO_RIO_PWM_2 = 2
ROBO_RIO_PWM_3 = 3
ROBO_RIO_PWM_4 = 4
ROBO_RIO_PWM_5 = 5
ROBO_RIO_PWM_6 = 6
ROBO_RIO_PWM_7 = 7
ROBO_RIO_PWM_8 = 8
ROBO_RIO_PWM_9 = 9

ROBO_RIO_DIO_0 = 0
ROBO_RIO_DIO_1 = 1
ROBO_RIO_DIO_2 = 2
ROBO_RIO_DIO_3 = 3
ROBO_RIO_DIO_4 = 4
ROBO_RIO_DIO_5 = 5
ROBO_RIO_DIO_6 = 6
ROBO_RIO_DIO_7 = 7
ROBO_RIO_DIO_8 = 8
ROBO_RIO_DIO_9 = 9

ROBO_RIO_NAVX_PWM_0 = navx.pins.getNavxPWMChannel(0)
ROBO_RIO_NAVX_PWM_1 = navx.pins.getNavxPWMChannel(1)
ROBO_RIO_NAVX_PWM_2 = navx.pins.getNavxPWMChannel(2)
ROBO_RIO_NAVX_PWM_3 = navx.pins.getNavxPWMChannel(3)
ROBO_RIO_NAVX_PWM_4 = navx.pins.getNavxPWMChannel(4)
ROBO_RIO_NAVX_PWM_5 = navx.pins.getNavxPWMChannel(5)
ROBO_RIO_NAVX_PWM_6 = navx.pins.getNavxPWMChannel(6)
ROBO_RIO_NAVX_PWM_7 = navx.pins.getNavxPWMChannel(7)
ROBO_RIO_NAVX_PWM_8 = navx.pins.getNavxPWMChannel(8)
ROBO_RIO_NAVX_PWM_9 = navx.pins.getNavxPWMChannel(9)

ROBO_RIO_NAVX_DIO_0 = navx.pins.getNavxDigitalChannel(0)
ROBO_RIO_NAVX_DIO_1 = navx.pins.getNavxDigitalChannel(1)
ROBO_RIO_NAVX_DIO_2 = navx.pins.getNavxDigitalChannel(2)
ROBO_RIO_NAVX_DIO_3 = navx.pins.getNavxDigitalChannel(3)
ROBO_RIO_NAVX_DIO_4 = navx.pins.getNavxDigitalChannel(4)
ROBO_RIO_NAVX_DIO_5 = navx.pins.getNavxDigitalChannel(5)
ROBO_RIO_NAVX_DIO_6 = navx.pins.getNavxDigitalChannel(6)
ROBO_RIO_NAVX_DIO_7 = navx.pins.getNavxDigitalChannel(7)
ROBO_RIO_NAVX_DIO_8 = navx.pins.getNavxDigitalChannel(8)
ROBO_RIO_NAVX_DIO_9 = navx.pins.getNavxDigitalChannel(9)

ROBO_RIO_RELAY_0 = 0
ROBO_RIO_RELAY_1 = 1
ROBO_RIO_RELAY_2 = 2
ROBO_RIO_RELAY_3 = 3

ROBO_RIO_ANALOG_IN_0 = 0
ROBO_RIO_ANALOG_IN_1 = 1
ROBO_RIO_ANALOG_IN_2 = 2
ROBO_RIO_ANALOG_IN_3 = 3

ROBO_RIO_ANALOG_IN_0 = navx.pins.getNavxAnalogInChannel(0)
ROBO_RIO_ANALOG_IN_1 = navx.pins.getNavxAnalogInChannel(1)
ROBO_RIO_ANALOG_IN_2 = navx.pins.getNavxAnalogInChannel(2)
ROBO_RIO_ANALOG_IN_3 = navx.pins.getNavxAnalogInChannel(3)

ROBO_RIO_ANALOG_OUT_0 = navx.pins.getNavxAnalogOutChannel(0)
ROBO_RIO_ANALOG_OUT_1 = navx.pins.getNavxAnalogOutChannel(1)

# pcm 

PCM_PORT_0 =  0  
PCM_PORT_1 =  1
PCM_PORT_2 =  2
PCM_PORT_3 =  3
PCM_PORT_4 =  4
PCM_PORT_5 =  5
PCM_PORT_6 =  6
PCM_PORT_7 =  7 

# outputs

PWM_FRONT_LEFT_A = ROBO_RIO_PWM_0
PWM_FRONT_RIGHT_A = ROBO_RIO_PWM_1

#WRIST =                 ROBO_RIO_PWM_8

INTAKE =                ROBO_RIO_PWM_9

HATCH_EXTEND =          PCM_PORT_0
HATCH_RETRACT =         PCM_PORT_2

LIFT_RETRACT =          PCM_PORT_1
LIFT_EXTEND =           PCM_PORT_3

SUSPENSION_RETRACT =    PCM_PORT_5
SUSPENSION_EXTEND =     PCM_PORT_6

CAN_PCM = 0
CAN_PDP = 62

CAN_LEFT_SHOULDER = 50
CAN_RIGHT_SHOULDER = 51

CAN_RIGHT_ELBOW = 52
CAN_LEFT_ELBOW = 53

CAN_WRIST = 54

CAN_REAR_RIGHT_A = 56
CAN_REAR_RIGHT_B = 57
CAN_REAR_LEFT_A = 58
CAN_REAR_LEFT_B = 59




# inputs

FRONT_RIGHT_ENCODER_A = ROBO_RIO_DIO_6
FRONT_RIGHT_ENCODER_B = ROBO_RIO_DIO_7
FRONT_LEFT_ENCODER_A =  ROBO_RIO_DIO_8
FRONT_LEFT_ENCODER_B =  ROBO_RIO_DIO_9 
REAR_LEFT_ENCODER_A =   ROBO_RIO_NAVX_DIO_0
REAR_LEFT_ENCODER_B =   ROBO_RIO_NAVX_DIO_1
REAR_RIGHT_ENCODER_A =  ROBO_RIO_NAVX_DIO_2
REAR_RIGHT_ENCODER_B =  ROBO_RIO_NAVX_DIO_3

SHOULDER_ENCODER_A =    ROBO_RIO_DIO_0
SHOULDER_ENCODER_B =    ROBO_RIO_DIO_1

ELBOW_ENCODER_A =       ROBO_RIO_DIO_2
ELBOW_ENCODER_B =       ROBO_RIO_DIO_3

WRIST_ENCODER_A =       ROBO_RIO_DIO_4
WRIST_ENCODER_B =       ROBO_RIO_DIO_5



DRIVER_STATION_JOYSTICK_0 = 0
DRIVER_STATION_JOYSTICK_1 = 1
DRIVER_STATION_JOYSTICK_2 = 2
DRIVER_STATION_JOYSTICK_3 = 3

ENCODER_DISTANCE_PER_PULSE = 1

SHOULDER_ELBOW_LENGTH = 29
ELBOW_WRIST_LENGTH = 24
WRIST_INTAKE_LENGTH = 15 

DRIVETRAIN_GEAR_RATIO = 50/11 * 54/20
DRIVETRAIN_WHEEL_DIAMETER = .66666 #8 in = 2/3 ft
DRIVE_TRAIN_FPS_FACTOR = 1 / DRIVETRAIN_GEAR_RATIO / 60 * DRIVETRAIN_WHEEL_DIAMETER * math.pi # native encoder units (rpm) / gear ratio / seconds in a minute * distance per revoluation

SHOULDER_GEAR_RATIO = 4 * 4 * 5 * (22/12)

ELBOW_GEAR_RATIO = 4 * 4 * 5 * (22/12)

WRIST_GEAR_RATIO = 4 * 5 * 5 * (22/12)

SHOULDER_DEGREES_FACTOR = 360 / SHOULDER_GEAR_RATIO
ELBOW_DEGREES_FACTOR = 360 / ELBOW_GEAR_RATIO
WRIST_DEGREES_FACTOR = 360 / WRIST_GEAR_RATIO

SHOULDER_START_POSITION = 76.5
ELBOW_START_POSITION = 107.4
WRIST_START_POSITION = 82.7

DRIVE_INPUT_Y_AXIS_MULTIPLIER = 0.75
DRIVE_INPUT_X_AXIS_MULTIPLIER = 0.7

DRIVETRAIN_PID_MAX = 10

DIVISIONS_PER_SECOND = 1000 / 20 #(ms per second over ms between control iterations in periodic)

SHOULDER_MAX_DEGREES_PER_SECOND = 180 / DIVISIONS_PER_SECOND
ELBOW_MAX_DEGREES_PER_SECOND = 180 / DIVISIONS_PER_SECOND
WRIST_MAX_DEGREES_PER_SECOND = 180 / DIVISIONS_PER_SECOND

DRIVETRAIN_USE_PID = False

SEND_DATA = True

SERVO_INCREMENT = 0.02
CAMERA_1_PWM = ROBO_RIO_PWM_6
CAMERA_2_PWM = ROBO_RIO_PWM_7
CAMERA_1_DEFAULT = 0.5
CAMERA_2_DEFAULT = 0.5

MOVE_SHOULDER_ELBOW_MIN = 80
MOVE_SHOULDER_ELBOW_MAX = 120

MOVE_ELBOW_SHOULDER_MIN = 115

SHOULDER_SETPOINT_MIN = 20.0
SHOULDER_SETPOINT_MAX = 138

ELBOW_BALL_PICKUP_POSITION = 238.0
WRIST_BALL_PICKUP_POSITION = 36.5
SHOULDER_BALL_PICKUP_POSITION = 28.2

ELBOW_BALL_SCORING_POSITION = 306.3
WRIST_BALL_SCORING_POSITION = 47.2
SHOULDER_BALL_SCORING_POSITION = 28.2

AUTOMATIC_ARM_MAXIMUM = 0.35
AUTOMATIC_ARM_MINIMUM = -0.35

ELBOW_AUTOMATIC_MAXIMUM = 0.45
ELBOW_AUTOMATIC_MINIMUM = -0.45

SHOULDER_TOWER_POSITION = SHOULDER_SETPOINT_MAX 
ELBOW_TOWER_POSITION = ELBOW_START_POSITION
WRIST_TOWER_POSITION = WRIST_START_POSITION