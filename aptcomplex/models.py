from django.db import models

# Create your models here.

class Houseinfo(models.Model):
    BUILDING_NUM_CHOICES = (
        (101, '101동'),
        (102, '102동'),
        (103, '103동'),
        (104, '104동'),
        (105, '105동'),
        (106, '106동'),
        (107, '107동'),
    )
    building_num = models.IntegerField(choices = BUILDING_NUM_CHOICES, default = "")
    HOUSE_NUM_CHOICES = (
        (101, '101호'),(102, '102호'),(103, '103호'),(104, '104호'),(105, '105호'),(106, '106호'),(107, '107호'),
        (201, '201호'),(202, '202호'),(203, '203호'),(204, '204호'),(205, '205호'),(206, '206호'),(207, '207호'),
        (301, '301호'),(302, '302호'),(303, '303호'),(304, '304호'),(305, '305호'),(306, '306호'),(307, '307호'),
        (401, '401호'),(402, '402호'),(403, '403호'),(404, '404호'),(405, '405호'),(406, '406호'),(407, '407호'),
        (501, '501호'),(502, '502호'),(503, '503호'),(504, '504호'),(505, '505호'),(506, '506호'),(507, '507호'),
        (601, '601호'),(602, '602호'),(603, '603호'),(604, '604호'),(605, '605호'),(606, '606호'),(607, '607호'),
        (701, '701호'),(702, '702호'),(703, '703호'),(704, '704호'),(705, '705호'),(706, '706호'),(707, '707호'),
        (801, '801호'),(802, '802호'),(803, '803호'),(804, '804호'),(805, '805호'),(806, '806호'),(807, '807호'),
        (901, '901호'),(902, '902호'),(903, '903호'),(904, '904호'),(905, '905호'),(906, '906호'),(907, '907호'),
        (1001, '1001호'),(1002, '1002호'),(1003, '1003호'),(1004, '1004호'),(1005, '1005호'),(1006, '1006호'),(1007, '1007호'),
        (1101, '1101호'),(1102, '1102호'),(1103, '1103호'),(1104, '1104호'),(1105, '1105호'),(1106, '1106호'),(1107, '1107호'),
        (1201, '1201호'),(1202, '1202호'),(1203, '1203호'),(1204, '1204호'),(1205, '1205호'),(1206, '1206호'),(1207, '1207호'),
        (1301, '1301호'),(1302, '1302호'),(1303, '1303호'),(1304, '1304호'),(1305, '1305호'),(1306, '1306호'),(1307, '1307호'),
        (1401, '1401호'),(1402, '1402호'),(1403, '1403호'),(1404, '1404호'),(1405, '1405호'),(1406, '1406호'),(1407, '1407호'),
        (1501, '1501호'),(1502, '1502호'),(1503, '1503호'),(1504, '1504호'),(1505, '1505호'),(1506, '1506호'),(1507, '1507호'),
    )
    house_num = models.IntegerField(choices = HOUSE_NUM_CHOICES, default ="")
    house_holder = models.CharField(max_length = 16, blank = True)

    def __str__(self):
        return str(self.building_num) + "동" + str(self.house_num) +"호"

    def get_building_num(self):
        return self.building_num

    def get_house_num(self):
        return self.house_num

    def get_house_holder(self):
        return self.house_holder