from MPU6050 import MPU6050

class Dice:
    def __init__(self):
        self.mpu = MPU6050()
        
    def getDeviceByNumber(self, number):
        devices = [{
            'name': 'TV'
        }, {
            'name': 'Evan\'s AC'
        }, {
            'name': 'Parents\' AC'
        }, {
            'name': 'Kitchen Lights'
        }, {
            'name': 'Main Door Lights'
        }, {
            'name': 'Living Room Lights'
        }, {
        }]
        
        return devices[number]
            
    def roll(self):
        THRESHOLD = 7
        accel = self.mpu.read_accel_data() # read the accelerometer [ms^-2]
        aX = accel["x"]
        aY = accel["y"]
        aZ = accel["z"]

    #    print (f'Y: {accel["y"]}')
        if accel["x"] > THRESHOLD:
            return 3
        elif accel["x"] < -THRESHOLD:
            return 2
        elif accel['y'] > THRESHOLD:
            return 4
        elif accel['y'] < -THRESHOLD:
            return 5
        elif accel['z'] > 0:
            return 1
        else:
            return 6
#        print("x: " + str(aX) + " y: " + str(aY) + " z: " + str(aZ))
        return 6
