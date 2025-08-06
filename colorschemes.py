#!/usr/bin/env python
# coding: utf-8

import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# color scheme class: an inner class that has individual color schemes 

class ColorScheme:
    def __init__(self, name, colors, harmony):
        # name: usually just the base color of the scheme with a number next to it
        # colors: a list of hexcode strings that are inside each color
        # harmony: monochromatric, complementary, triadic, etc 
        self.name = name
        self.colors = colors
        self.harmony = harmony
    
    def __repr__(self):
        return f"ColorScheme(name='{self.name}', colors={len(self.colors)} colors)"

    
# big class that contains all the colors I like wish me luck
class color_schemes:
    def __init__(self):
        # use the ColorScheme class to define all of the colors you like here
        
        # page 26
        self.red1 = ColorScheme(
            name='red1',
            colors=['#FFFAFA','#ECDBD2','#EDC1AF','#F18A81','#DF4E41'],
            harmony='monochromatic'
        )
        
        self.red2 = ColorScheme(
            name='red2',
            colors=['#C43153','#D15471','#D98296','#C4C4C4','#DAE8E6'],
            harmony='monochromatic'
        )
        
        self.red3 = ColorScheme(
            name='red3',
            colors=['#BFB9A7','#B4938D','#A86D74','#9D475A','#912142'],
            harmony='monochromatic'
        )
        
        # page 27
        self.red4 = ColorScheme(
            name='red4',
            colors=['#450408','#560300','#7E0A0D','#A70000','#FF7245'],
            harmony='monochromatic'
        )
        
        self.red5 = ColorScheme(
            name='red5',
            colors=['#F52525','#F54C4C','#F57373','#F59A9A','#F5C1C1'],
            harmony='monochromatic'
        )
        
        # page 28
        self.red6 = ColorScheme(
            name='red6',
            colors=['#DA5E5C','#AF2D2D','#963839','#771417','#64090E'],
            harmony='monochromatic'
        )
        
        self.red7 = ColorScheme(
            name='red7',
            colors=['#7D2758','#D12D52','#FE4844','#FF8787','#FFB3B3'],
            harmony='analogous'
        )
        
        self.red8 = ColorScheme(
            name='red8',
            colors=['#F2CB7E','#FFA46B','#ff5e5e','#ff335c','#eb054d'],
            harmony='analogous'
        )
        
        self.red9 = ColorScheme(
            name='red9',
            colors=['#ffab49','#ffc684','#e55584','#b73b50','#71202e'],
            harmony='analogous'
        )
        
        self.red10 = ColorScheme(
            name='red10',
            colors=['#ffcb8b','#ff9d78','#ff6b68','#ff4f5e','#ff2458'],
            harmony='analogous'
        )
        
        self.red11 = ColorScheme(
            name='red11',
            colors=['#f29e99','#eea595','#e9ad8f','#e5b58a','#dec083'],
            harmony='analogous'
        )
        
        # page 29
        self.red12 = ColorScheme(
            name='red12',
            colors=['#f2eee2','#e8e2cc','#d6b99b','#b55862','#8a2f34'],
            harmony='analogous'
        )
        
        self.red13 = ColorScheme(
            name='red13',
            colors=['#daef2d','#f0a63c','#ed503b','#be0237','#840b3b'],
            harmony='analogous'
        )
        
        self.red14 = ColorScheme(
            name='red14',
            colors=['#ffc55f','#ed7850','#d5485b','#b54780','#895284'],
            harmony='analogous'
        )
        
        self.red15 = ColorScheme(
            name='red15',
            colors=['#751e2a','#a82c2e','#cc2f56','#f29148','#ffc457'],
            harmony='analogous'
        )
        
        # page 30
        self.red16 = ColorScheme(
            name='red16',
            colors=['#002d70','#0091ff','#ff0011','#ff6f00','#ffee00'],
            harmony='triadic'
        )
        
        self.red17 = ColorScheme(
            name='red17',
            colors=['#234568','#fffd59','#ffaf66','#ff6850','#f35857'],
            harmony='triadic'
        )
        
        # page 31
        self.red18 = ColorScheme(
            name='red18',
            colors=['#96130C','#c64031','#f2ac0a','#ebe696','#13ac96'],
            harmony='triadic'
        )
        
        # page 32
        self.red19 = ColorScheme(
            name='red19',
            colors=['#177A65','#f8f0a5','#eebc4b','#ce6e0a','#be0d07'],
            harmony='split-complementary'
        )
        
        self.red20 = ColorScheme(
            name='red20',
            colors=['#c7c39d','#59967e','#546472','#4f3f4b','#cc3151'],
            harmony='split-complementary'
        )
        
        self.red21 = ColorScheme(
            name='red21',
            colors=['#15354A','#A8DEA6','#F7F7BC','#f57f63','#d63a3a'],
            harmony='split-complementary'
        )
        
        # page 33
        self.red22 = ColorScheme(
            name='red22',
            colors=['#09668c','#acadca','#e6e971','#df3d22','#a90801'],
            harmony='split-complementary'
        )
        
        self.red23 = ColorScheme(
            name='red23',
            colors=['#cd375c','#842042','#57b497','#dad869','#fbe09d'],
            harmony='split-complementary'
        )
        
        self.red24 = ColorScheme(
            name='red24',
            colors=['#9d2030','#ff4e6b','#fe964d','#b7be3c','#2a6851'],
            harmony='split-complementary'
        )
        
        # page 34
        self.red25 = ColorScheme(
            name='red25',
            colors=['#f81e5c','#e9537c','#da889c','#cbbdbc','#bcf3dc'],
            harmony='complementary'
        )
        
        self.red26 = ColorScheme(
            name='red26',
            colors=['#800618','#c9364f','#f0638a','#c9c536','#f0ec73'],
            harmony='complementary'
        )
        
        self.red27 = ColorScheme(
            name='red27',
            colors=['#7e7e00','#f0dca9','#c05100','#b60004','#800000'],
            harmony='complementary'
        )
        
        self.red28 = ColorScheme(
            name='red28',
            colors=['#7e7e00','#f0dca9','#c05100','#b60004','#800000'],
            harmony='complementary'
        )
        
        self.red29 = ColorScheme(
            name='red29',
            colors=['#b0c093','#d9d9a9','#eac7a4','#edaa98','#b7375f'],
            harmony='complementary'
        )
        
        self.red30 = ColorScheme(
            name='red30',
            colors=['#82c598','#7f9876','#7d6b53','#7c3f31','#790706'],
            harmony='complementary'
        )
        
        # page 35
        self.red31 = ColorScheme(
            name='red31',
            colors=['#ED6D6E','#B55151','#FFFCCC','#8DB593','#58755C'],
            harmony='complementary'
        )
        
        # page 36
        self.red32 = ColorScheme(
            name='red32',
            colors=['#262525','#525252','#E6DDBC','#822626','#690202'],
            harmony='other'
        )
        
        self.red33 = ColorScheme(
            name='red33',
            colors=['#D8DEB6','#8AB8AA','#C4273A','#61292D','#2B2424'],
            harmony='other'
        )
        
        self.red34 = ColorScheme(
            name='red34',
            colors=['#356272','#280101','#82162C','#B8242D','#CD5C44'],
            harmony='other'
        )
        
        self.red35 = ColorScheme(
            name='red35',
            colors=['#062F43','#3D464D','#F5DA2C','#F2792E','#D82125'],
            harmony='other'
        )
        
        self.red36 = ColorScheme(
            name='red36',
            colors=['#FFA408','#FF4747','#E81D1D','#BD0420','#3C0444'],
            harmony='other'
        )
        
        self.red37 = ColorScheme(
            name='red37',
            colors=['#8D505A','#8B797F','#89A1A3','#BEBD8C','#F2D974'],
            harmony='other'
        )
        
        # page 37
        self.red38 = ColorScheme(
            name='red38',
            colors=['#F7F8D2','#F84129','#F89F2E','#0A3A5F','#9E1E4C'],
            harmony='other'
        )
        
        self.red39 = ColorScheme(
            name='red39',
            colors=['#880000','#883333','#886666','#889999','#88CCCC'],
            harmony='other'
        )
        
        self.red40 = ColorScheme(
            name='red40',
            colors=['#6B455C','#703142','#991F36','#AD3736','#B8A45B'],
            harmony='other'
        )
        
        self.red41 = ColorScheme(
            name='red41',
            colors=['#EBE7A4','#BBD66F','#BDA22A','#CC6A2D','#BD2F42'],
            harmony='other'
        )
        
        # page 39
        self.red_orange1 = ColorScheme(
            name='red_orange1',
            colors=['#C91B00','#C93C26','#C95D4D','#C97E73','#C9A099'],
            harmony='monochromatic'
        )
        
        self.red_orange2 = ColorScheme(
            name='red_orange2',
            colors=['#bd2323','#d1371d','#dd542d','#e87c4e','#f7e2a3'],
            harmony='monochromatic'
        )
        
        self.red_orange3 = ColorScheme(
            name='red_orange3',
            colors=['#997E71','#9C654B','#AC542B','#C44D16','#E74C05'],
            harmony='monochromatic'
        )
        
        self.red_orange4 = ColorScheme(
            name='red_orange4',
            colors=['#997E71','#9C654B','#AC542B','#C44D16','#E74C05'],
            harmony='monochromatic'
        )
        
        # page 40
        self.red_orange5 = ColorScheme(
            name='red_orange5',
            colors=['#ED7858','#DB8067','#BF7F6D','#967B77','#695F5E'],
            harmony='monochromatic'
        )
        
        self.red_orange6 = ColorScheme(
            name='red_orange6',
            colors=['#F7E1CA','#F3C1A7','#EFA185','#EB8163','#E76241'],
            harmony='monochromatic'
        )

        # page 41
        self.red_orange7 = ColorScheme(
            name='red_orange7',
            colors=['#8E324C','#563750','#3E3951','#A14B4A','#CC5247'],
            harmony='analogous'
        )
        
        self.red_orange8 = ColorScheme(
            name='red_orange8',
            colors=['#FF7474','#F59B71','#C7C77F','#E0E0A8','#F1F1C1'],
            harmony='analogous'
        )
        
        self.red_orange9 = ColorScheme(
            name='red_orange9',
            colors=['#FF8F74','#FFB274','#FFD573','#FFF873','#E3FF73'],
            harmony='analogous'
        )
        
        self.red_orange10 = ColorScheme(
            name='red_orange10',
            colors=['#FCC896','#FAAE7D','#E67E65','#D76042','#B8472E'],
            harmony='analogous'
        )
        
        # page 42
        self.red_orange11 = ColorScheme(
            name='red_orange11',
            colors=['#FE5838','#FE775D','#FFE7AE','#FFD265','#AB7966'],
            harmony='analogous'
        )
        
        # page 43
        self.red_orange12 = ColorScheme(
            name='red_orange12',
            colors=['#D95B59','#D98E59','#D9CC59','#ECF5D3','#7A75D9'],
            harmony='triadic'
        )
        
        self.red_orange13 = ColorScheme(
            name='red_orange13',
            colors=['#101A4B','#0A3F0E','#C42809','#EE7E15'],
            harmony='triadic'
        )
        
        self.red_orange14 = ColorScheme(
            name='red_orange14',
            colors=['#544661','#56718F','#70947F','#B1B090','#C05B5B'],
            harmony='triadic'
        )
        
        # page 45
        self.red_orange15 = ColorScheme(
            name='red_orange15',
            colors=['#2A1842','#9B1A29','#D35E53','#6BC7A5','#3DB8B4'],
            harmony='split-complementary'
        )
        
        self.red_orange16 = ColorScheme(
            name='red_orange16',
            colors=['#E65540','#F8ECC2','#65A8A6','#79896D'],
            harmony='split-complementary'
        )
        
        # page 46
        self.red_orange17 = ColorScheme(
            name='red_orange17',
            colors=['#AFDEF8','#E6986B','#E6B56B','#F1E49F','#2EA24F'],
            harmony='split-complementary'
        )
        
        self.red_orange18 = ColorScheme(
            name='red_orange18',
            colors=['#FF935C','#FFDF5F','#AAFF60','#62FFBC','#5E96FF'],
            harmony='split-complementary'
        )
        
        self.red_orange19 = ColorScheme(
            name='red_orange19',
            colors=['#001860','#036B2E','#F09000','#F06018','#C00000'],
            harmony='split-complementary'
        )
        
        self.red_orange20 = ColorScheme(
            name='red_orange20',
            colors=['#91FFC8','#D1EDFF','#FFF596','#FFAD29','#DE351B'],
            harmony='split-complementary'
        )
        
        self.red_orange21 = ColorScheme(
            name='red_orange21',
            colors=['#D83030','#D86048','#D8A860','#789078','#303048'],
            harmony='split-complementary'
        )
        
        self.red_orange22 = ColorScheme(
            name='red_orange22',
            colors=['#312E50','#4DBD90','#F8D989','#FF774B','#D11258'],
            harmony='split-complementary'
        )
        
        # page 47
        self.red_orange23 = ColorScheme(
            name='red_orange23',
            colors=['#66CC99','#80A673','#99804D','#B35926','#CC3300'],
            harmony='complementary'
        )
        
        self.red_orange24 = ColorScheme(
            name='red_orange24',
            colors=['#042C30','#3A9177','#84E3C6','#EB5B34','#BA3925'],
            harmony='complementary'
        )
        
        # page 48
        self.red_orange25 = ColorScheme(
            name='red_orange25',
            colors=['#659FC5','#90C9E4','#D5F6E3','#FDBE9F','#FB7A50'],
            harmony='complementary'
        )
        
        self.red_orange26 = ColorScheme(
            name='red_orange26',
            colors=['#F0F0A3','#08CB9B','#097D7A','#253A52','#FC683F'],
            harmony='complementary'
        )
        
        # page 49
        self.red_orange27 = ColorScheme(
            name='red_orange27',
            colors=['#E1EDD1','#AAB69B','#9E906E','#B47941','#CF391D'],
            harmony='other'
        )
        
        self.red_orange28 = ColorScheme(
            name='red_orange28',
            colors=['#74BFC2','#8F6089','#E05A5E','#F77736','#F7CE36'],
            harmony='other'
        )
        
        self.red_orange29 = ColorScheme(
            name='red_orange29',
            colors=['#181419','#4A073C','#9E0B41','#CC3E18','#F0971C'],
            harmony='other'
        )
        
        self.red_orange30 = ColorScheme(
            name='red_orange30',
            colors=['#FDB252','#FB8E4D','#FA6A48','#A77D67','#549187'],
            harmony='other'
        )
        
        self.red_orange31 = ColorScheme(
            name='red_orange31',
            colors=['#D63E1B','#C48C53','#B3B07E','#8DC5AE','#89E2EE'],
            harmony='other'
        )
        
        # page 50
        self.red_orange32 = ColorScheme(
            name='red_orange32',
            colors=['#FF8F5E','#FFD9A3','#B8B588','#486B5F','#1D192E'],
            harmony='other'
        )
        
        self.red_orange33 = ColorScheme(
            name='red_orange33',
            colors=['#ECD078','#D95B43','#C02942','#542437','#53777A'],
            harmony='other'
        )
        
        self.red_orange34 = ColorScheme(
            name='red_orange34',
            colors=['#69666E','#E8805D','#E6AA65','#D9D584','#F2E79D'],
            harmony='other'
        )
        
        self.red_orange35 = ColorScheme(
            name='red_orange35',
            colors=['#489991','#C7CF8F','#FFA852','#E36249','#4F442A'],
            harmony='other'
        )
        
        # page 51
        self.orange1 = ColorScheme(
            name='orange1',
            colors=['#FF4F1F','#FF6619','#FF7A38','#FF8F33','#FFA640'],
            harmony='monochromatic'
        )
        
        # page 52
        self.orange2 = ColorScheme(
            name='orange2',
            colors=['#F7F5F4','#FFE2D3','#FFCAAF','#FFB48F','#FF935E'],
            harmony='monochromatic'
        )
        
        # page 53
        self.orange3 = ColorScheme(
            name='orange3',
            colors=['#523A36','#8F4D2C','#B8772E','#C79B5D','#C4A984'],
            harmony='monochromatic'
        )
        
        # page 55
        self.orange4 = ColorScheme(
            name='orange4',
            colors=['#FEFCA5','#F5B971','#BE9569','#988368','#4C4952'],
            harmony='analogous'
        )
        
        # page 56
        self.orange5 = ColorScheme(
            name='orange5',
            colors=['#695C6E','#4396A6','#98F3D4','#F6E597','#FDA25B'],
            harmony='triadic'
        )
        
        self.orange6 = ColorScheme(
            name='orange6',
            colors=['#7EFFCD','#7EB0FF','#CD7DFF','#FF7DAF','#FFCD7D'],
            harmony='triadic'
        )
        
        self.orange7 = ColorScheme(
            name='orange7',
            colors=['#0E8C5C','#F0B70C','#F07007','#F00CB3','#AB0CF0'],
            harmony='triadic'
        )
        
        # page 58
        self.orange8 = ColorScheme(
            name='orange8',
            colors=['#0A3441','#2A1C1E','#6E1916','#BF100F','#FF4000'],
            harmony='split-complementary'
        )
        
        # page 59
        self.orange9 = ColorScheme(
            name='orange9',
            colors=['#454259','#618C70','#F2C46D','#F2AA6B','#D98162'],
            harmony='split-complementary'
        )
        
        self.orange10 = ColorScheme(
            name='orange10',
            colors=['#F5E28C','#D17F0D','#067B9E','#51379E','#262678'],
            harmony='split-complementary'
        )
        
        self.orange11 = ColorScheme(
            name='orange11',
            colors=['#2B5577','#4F457A','#753456','#B14B22','#E27927'],
            harmony='split-complementary'
        )
        
        # page 60
        self.orange12 = ColorScheme(
            name='orange12',
            colors=['#FF5C56','#FF9C56','#FFBE56','#3A6367','#34929B'],
            harmony='complementary'
        )
        
        self.orange13 = ColorScheme(
            name='orange13',
            colors=['#4F3B80','#3B6480','#3B807C','#DEB045','#C27202'],
            harmony='complementary'
        )
        
        self.orange14 = ColorScheme(
            name='orange14',
            colors=['#FF8800','#FFA602','#8CFFF0','#2160D4','#1D03A1'],
            harmony='complementary'
        )
        
        # page 61
        self.orange15 = ColorScheme(
            name='orange15',
            colors=['#1F6BB3','#557595','#8B7F76','#C18858','#F79239'],
            harmony='complementary'
        )
        
        self.orange16 = ColorScheme(
            name='orange16',
            colors=['#FDAA5D','#E9B284','#D5B9AC','#C0C1D3','#ACC8FA'],
            harmony='complementary'
        )
        
        # page 62
        self.orange17 = ColorScheme(
            name='orange17',
            colors=['#181419','#4A073C','#9E0B41','#CC3E18','#F0971C'],
            harmony='other'
        )
        
        self.orange18 = ColorScheme(
            name='orange18',
            colors=['#265C52','#76564D','#C55048','#DA6F43','#EB9944'],
            harmony='other'
        )
        
        self.orange19 = ColorScheme(
            name='orange19',
            colors=['#332F4A','#4D4839','#965A35','#FC6753','#FFA733'],
            harmony='other'
        )
        
        self.orange20 = ColorScheme(
            name='orange20',
            colors=['#FFA623','#C4A622','#82912B','#4C6954','#2A4042'],
            harmony='other'
        )
        
        # page 65
        self.orange_yellow1 = ColorScheme(
            name='orange_yellow1',
            colors=['#CC933D','#E2A947','#EEB24B','#F8BA4E','#FFBE4E'],
            harmony='monochromatic'
        )
        
        self.orange_yellow2 = ColorScheme(
            name='orange_yellow2',
            colors=['#F3CF00','#F5D742','#F7DF88','#F9E7CE','#FBEFFF'],
            harmony='monochromatic'
        )
        
        # page 66
        self.orange_yellow3 = ColorScheme(
            name='orange_yellow3',
            colors=['#B17C36','#F2AD4B','#FFDA82','#FFE4A6','#FFF3D6'],
            harmony='monochromatic'
        )
        
        self.orange_yellow4 = ColorScheme(
            name='orange_yellow4',
            colors=['#DDEAF2','#E5E6D6','#ECE2BA','#F4DD9E','#FBD982'],
            harmony='monochromatic'
        )
        
        # page 67
        self.orange_yellow5 = ColorScheme(
            name='orange_yellow5',
            colors=['#FCF39F','#F0E47D','#E6AB5A','#A65858','#7A3333'],
            harmony='analogous'
        )
        
        self.orange_yellow6 = ColorScheme(
            name='orange_yellow6',
            colors=['#BC2125','#5F0101','#A3AB3C','#FFD203','#FFB808'],
            harmony='analogous'
        )
        
        self.orange_yellow7 = ColorScheme(
            name='orange_yellow7',
            colors=['#F5CA00','#E4CA00','#D3CA00','#C2CA00','#B1CA00'],
            harmony='analogous'
        )
        
        self.orange_yellow8 = ColorScheme(
            name='orange_yellow8',
            colors=['#E6AC00','#A15E00','#662700','#360300','#1F000B'],
            harmony='analogous'
        )
        
        self.orange_yellow9 = ColorScheme(
            name='orange_yellow9',
            colors=['#FFE880','#CBF299','#C6D9A3','#A3A3A3','#A68385'],
            harmony='analogous'
        )
        
        # page 68
        self.orange_yellow10 = ColorScheme(
            name='orange_yellow10',
            colors=['#D9BA6C','#A4AD83','#7B9484','#774D73','#8F1E61'],
            harmony='analogous'
        )
        
        self.orange_yellow11 = ColorScheme(
            name='orange_yellow11',
            colors=['#827160','#9EA4AD','#F5ECA9','#EBCF75','#CCA752'],
            harmony='analogous'
        )
        
        self.orange_yellow12 = ColorScheme(
            name='orange_yellow12',
            colors=['#F0A639','#DFB55A','#CDC47B','#BCD39B','#AAE2BC'],
            harmony='analogous'
        )
        
        self.orange_yellow13 = ColorScheme(
            name='orange_yellow13',
            colors=['#FFF9C2','#EBCC42','#BA652D','#A20041','#850C38'],
            harmony='analogous'
        )
        
        self.orange_yellow14 = ColorScheme(
            name='orange_yellow14',
            colors=['#FFC948','#EDBA42','#C9B144','#B85362','#A84755'],
            harmony='analogous'
        )
        
        # page 69
        self.orange_yellow15 = ColorScheme(
            name='orange_yellow15',
            colors=['#FFDF6B','#DBB630','#572146','#472157','#364463'],
            harmony='triadic'
        )
        
        self.orange_yellow16 = ColorScheme(
            name='orange_yellow16',
            colors=['#6E2052','#F99857','#F4D983','#7DBDA4','#669A85'],
            harmony='triadic'
        )
        
        # page 70
        self.orange_yellow17 = ColorScheme(
            name='orange_yellow17',
            colors=['#FFDB55','#BBAF5B','#648360','#8C5162','#B41F63'],
            harmony='triadic'
        )
        
        self.orange_yellow18 = ColorScheme(
            name='orange_yellow18',
            colors=['#C46D16','#E8C93F','#3FE885','#478F8B','#6B2561'],
            harmony='triadic'
        )
        
        self.orange_yellow19 = ColorScheme(
            name='orange_yellow19',
            colors=['#480030','#F0C048','#F0D878','#487860','#486048'],
            harmony='triadic'
        )
        
        # page 71
        self.orange_yellow20 = ColorScheme(
            name='orange_yellow20',
            colors=['#FFED90','#A8D46F','#359668','#3C3251','#341139'],
            harmony='split-complementary'
        )
        
        self.orange_yellow21 = ColorScheme(
            name='orange_yellow21',
            colors=['#5B4E69','#8095AB','#B4D2DE','#F5F2ED','#FFE6B3'],
            harmony='split-complementary'
        )
        
        self.orange_yellow22 = ColorScheme(
            name='orange_yellow22',
            colors=['#0E6A9C','#611F80','#BE338C','#E77E1C','#E5BA36'],
            harmony='split-complementary'
        )
        
        self.orange_yellow23 = ColorScheme(
            name='orange_yellow23',
            colors=['#F0BE07','#FD9427','#C71418','#751A39','#33565C'],
            harmony='split-complementary'
        )
        
        self.orange_yellow24 = ColorScheme(
            name='orange_yellow24',
            colors=['#88CBF7','#88BEF7','#EEB2F7','#FFD7B0','#FFE7B0'],
            harmony='split-complementary'
        )
        
        self.orange_yellow25 = ColorScheme(
            name='orange_yellow25',
            colors=['#A0A4DC','#BFAB9C','#DFB35C','#E690A4','#EE6EEC'],
            harmony='split-complementary'
        )
        
        # page 72
        self.orange_yellow26 = ColorScheme(
            name='orange_yellow26',
            colors=['#FFE570','#EB8888','#AB5E86','#754585','#3B386E'],
            harmony='split-complementary'
        )
        
        self.orange_yellow27 = ColorScheme(
            name='orange_yellow27',
            colors=['#FFEA9F','#F7CF6D','#40939F','#4D4B9F','#6B2A7F'],
            harmony='split-complementary'
        )
        
        self.orange_yellow28 = ColorScheme(
            name='orange_yellow28',
            colors=['#F7DC70','#FFAE02','#AA5FB9','#0276B9','#06A3E0'],
            harmony='split-complementary'
        )
        
        self.orange_yellow29 = ColorScheme(
            name='orange_yellow29',
            colors=['#7878D2','#9D87C5','#9BAEAA','#FFD042','#F6AF33'],
            harmony='split-complementary'
        )
        
        self.orange_yellow30 = ColorScheme(
            name='orange_yellow30',
            colors=['#8B25CF','#94A8EB','#97E9F7','#F7E8C3','#F7BA1E'],
            harmony='split-complementary'
        )
        
        self.orange_yellow31 = ColorScheme(
            name='orange_yellow31',
            colors=['#721D61','#623C74','#535A88','#43799B','#F3D342'],
            harmony='split-complementary'
        )
        
        # page 73
        self.orange_yellow32 = ColorScheme(
            name='orange_yellow32',
            colors=['#FFB663','#FFE17D','#FFF3A8','#A880FF','#7752FF'],
            harmony='complementary'
        )
        
        self.orange_yellow33 = ColorScheme(
            name='orange_yellow33',
            colors=['#EBD652','#E6DB95','#B9ABD9','#6C6580','#7961B0'],
            harmony='complementary'
        )
        
        self.orange_yellow34 = ColorScheme(
            name='orange_yellow34',
            colors=['#3909AB','#320E8F','#E7BA09','#F9D322','#FFEF27'],
            harmony='complementary'
        )
        
        self.orange_yellow35 = ColorScheme(
            name='orange_yellow35',
            colors=['#FFEE99','#EEDDBB','#DDCCDD','#CCBBEE','#BBAAFF'],
            harmony='complementary'
        )
        
        # page 74
        self.orange_yellow36 = ColorScheme(
            name='orange_yellow36',
            colors=['#8ED4B7','#26ADAD','#9E5779','#B8750B','#D4AF0D'],
            harmony='complementary'
        )
        
        self.orange_yellow37 = ColorScheme(
            name='orange_yellow37',
            colors=['#F5D969','#D8BD8C','#BBA1AF','#9E85D2','#8169F5'],
            harmony='complementary'
        )
        
        # page 75
        self.orange_yellow38 = ColorScheme(
            name='orange_yellow38',
            colors=['#7A497A','#68687A','#499179','#90A848','#D4B855'],
            harmony='other'
        )
        
        self.orange_yellow39 = ColorScheme(
            name='orange_yellow39',
            colors=['#0B5F8A','#F5FFAB','#D9A223','#700052','#2F344D'],
            harmony='other'
        )
        
        self.orange_yellow40 = ColorScheme(
            name='orange_yellow40',
            colors=['#EDB314','#FAF8BF','#7DCD6C','#7F8A7C','#701840'],
            harmony='other'
        )
        
        self.orange_yellow41 = ColorScheme(
            name='orange_yellow41',
            colors=['#FFFF99','#D9CC8C','#B39980','#8C6673','#663366'],
            harmony='other'
        )
        
        # page 76
        self.orange_yellow42 = ColorScheme(
            name='orange_yellow42',
            colors=['#220B73','#243EA6','#88CC2F','#FFEA2E','#FFFA9C'],
            harmony='other'
        )
        
        self.orange_yellow43 = ColorScheme(
            name='orange_yellow43',
            colors=['#F1EA98','#F7D084','#ED967F','#DE7879','#C76783'],
            harmony='other'
        )
        
        self.orange_yellow44 = ColorScheme(
            name='orange_yellow44',
            colors=['#FEE4A9','#F7A50A','#115566','#AA151A','#0A0903'],
            harmony='other'
        )
        
        # page 79
        self.yellow1 = ColorScheme(
            name='yellow1',
            colors=['#E6F065','#D6CE2F','#9E970E','#57530A','#132607'],
            harmony='monochromatic'
        )
        
        # page 80
        self.yellow2 = ColorScheme(
            name='yellow2',
            colors=['#F7C605','#F7E017','#FCFF31','#E5E421','#CCD90C'],
            harmony='analogous'
        )
        
        self.yellow3 = ColorScheme(
            name='yellow3',
            colors=['#9BCD66','#C6D429','#E3DE69','#F1F473','#FFE83C'],
            harmony='analogous'
        )
        
        self.yellow4 = ColorScheme(
            name='yellow4',
            colors=['#C3FFBF','#8DFF85','#FF9C5E','#FFE985','#FFF9BF'],
            harmony='analogous'
        )
        
        self.yellow5 = ColorScheme(
            name='yellow5',
            colors=['#752914','#945421','#948821','#BDAD1C','#F5E873'],
            harmony='analogous'
        )
        
        self.yellow5 = ColorScheme(
            name='yellow5',
            colors=['#752914','#945421','#948821','#BDAD1C','#F5E873'],
            harmony='analogous'
        )
        
        # page 84 
        self.yellow6 = ColorScheme(
            name='yellow6',
            colors=['#EF14DE','#C000FF','#BDADDE','#E2ECC9','#FAFFBF'],
            harmony='split-complementary'
        )
        
        self.yellow7 = ColorScheme(
            name='yellow7',
            colors=['#FCF768','#FCF0B6','#C6CDFF','#C993FF','#9B518C'],
            harmony='split-complementary'
        )
        
        self.yellow8 = ColorScheme(
            name='yellow8',
            colors=['#EDAA53','#F8F371','#CFEDF8','#C7BAE5','#CB2B8B'],
            harmony='split-complementary'
        )
        
        self.yellow9 = ColorScheme(
            name='yellow9',
            colors=['#6B4264','#725EA6','#58A4A0','#9DD1AE','#F0EEA5'],
            harmony='split-complementary'
        )
        
        # page 85
        self.yellow10 = ColorScheme(
            name='yellow10',
            colors=['#A44C5F','#AE7AAB','#B8A8F7','#D2D385','#ECFE13'],
            harmony='split-complementary'
        )
        
        # page 86
        self.yellow11 = ColorScheme(
            name='yellow11',
            colors=['#5F3D66','#B721D9','#B38888','#C4B31A','#EEFF00'],
            harmony='complementary'
        )
        
        # page 87
        self.yellow12 = ColorScheme(
            name='yellow12',
            colors=['#FFE107','#DDCE5A','#A39EA7','#A689B9','#9513EC'],
            harmony='complementary'
        )
        
        # page 88
        self.yellow13 = ColorScheme(
            name='yellow13',
            colors=['#F6E100','#C7AB38','#99768F','#693FE4','#3908FF'],
            harmony='other'
        )
        
        # page 89
        self.yellow14 = ColorScheme(
            name='yellow14',
            colors=['#FAF5E6','#EBE45E','#99BB39','#469114','#030B2B'],
            harmony='other'
        )
        
        self.yellow15 = ColorScheme(
            name='yellow15',
            colors=['#4D1F26','#702647','#DB972A','#FFD94F','#FDFF6E'],
            harmony='other'
        )
        
        self.yellow16 = ColorScheme(
            name='yellow16',
            colors=['#303060','#486060','#C0D890','#F0F090','#F0F048'],
            harmony='other'
        )
        
        self.yellow17 = ColorScheme(
            name='yellow17',
            colors=['#25E6DC','#6AE6EB','#AEE5F2','#F5E0FF','#FFFBAB'],
            harmony='other'
        )
        
        self.yellow18 = ColorScheme(
            name='yellow18',
            colors=['#FAFFF9','#DCF7F6','#C6F5BA','#E0F29A','#F2EC78'],
            harmony='other'
        )
        
        # page 91
        self.yellow_green1 = ColorScheme(
            name='yellow_green1',
            colors=['#171F01','#526B01','#7FA601','#A8DB01','#C3FF01'],
            harmony='monochromatic'
        )
        
        # page 92
        self.yellow_green2 = ColorScheme(
            name='yellow_green2',
            colors=['#377437','#6CAC42','#77B924','#98CE56','#E8FDCD'],
            harmony='monochromatic'
        )
        
        # page 93
        self.yellow_green3 = ColorScheme(
            name='yellow_green3',
            colors=['#FCFA7E','#DBFC7E','#ADFC7E','#7EFCA8','#5AE0DA'],
            harmony='analogous'
        )
        
        self.yellow_green4 = ColorScheme(
            name='yellow_green4',
            colors=['#DD610F','#E69C1D','#DDC50F','#D5DD0F','#AFBB2C'],
            harmony='analogous'
        )
        
        # page 94
        self.yellow_green5 = ColorScheme(
            name='yellow_green5',
            colors=['#217B5A','#429452','#73B542','#8CC53B','#9CCE31'],
            harmony='analogous'
        )
        
        self.yellow_green6 = ColorScheme(
            name='yellow_green6',
            colors=['#E9FF3F','#C9FF3F','#9BFF3F','#65FF3F','#3FFF4E'],
            harmony='analogous'
        )
        
        # page 95
        self.yellow_green7 = ColorScheme(
            name='yellow_green7',
            colors=['#FFCDB7','#CDB7FF','#008E9E','#57FF52','#ADFF52'],
            harmony='triadic'
        )
        
        # page 96
        self.yellow_green8 = ColorScheme(
            name='yellow_green8',
            colors=['#C0CC50','#AD995A','#A66659','#A27790','#9D88C8'],
            harmony='triadic'
        )
        
        # page 97
        self.yellow_green9 = ColorScheme(
            name='yellow_green9',
            colors=['#51AEB5','#45487D','#775685','#C25F51','#C4C922'],
            harmony='split-complementary'
        )
        
        self.yellow_green10 = ColorScheme(
            name='yellow_green10',
            colors=['#CEF781','#A2A389','#754E91','#672749','#590000'],
            harmony='split-complementary'
        )
        
        # page 99
        self.yellow_green11 = ColorScheme(
            name='yellow_green11',
            colors=['#E02DDA','#CD5AAF','#BA8784','#A6B358','#93E02D'],
            harmony='complementary'
        )
        
        self.yellow_green12 = ColorScheme(
            name='yellow_green12',
            colors=['#BCCA92','#9CC09B','#989B89','#987072','#98465A'],
            harmony='complementary'
        )
        
        self.yellow_green13 = ColorScheme(
            name='yellow_green13',
            colors=['#CFD6A9','#6D926C','#75806A','#740B1C','#7F3D3D'],
            harmony='complementary'
        )
        
        self.yellow_green14 = ColorScheme(
            name='yellow_green14',
            colors=['#B3312D','#863A41','#5C3947','#8E9945','#D2F29D'],
            harmony='complementary'
        )
        
        self.yellow_green15 = ColorScheme(
            name='yellow_green15',
            colors=['#AA26FC','#B47DC1','#B9A8A3','#BDCF89','#C3FF68'],
            harmony='complementary'
        )
        
        # page 100
        self.yellow_green16 = ColorScheme(
            name='yellow_green16',
            colors=['#954D72','#A36E7E','#AB9587','#B5BC93','#E0FCC9'],
            harmony='complementary'
        )
        
        self.yellow_green17 = ColorScheme(
            name='yellow_green17',
            colors=['#705047','#EB6931','#FAAF2F','#DBC96B','#2F6F8A'],
            harmony='complementary'
        )
        
        # page 101
        self.yellow_green18 = ColorScheme(
            name='yellow_green18',
            colors=['#C4E096','#95A77F','#727C6E','#3B3953','#1D1342'],
            harmony='other'
        )
        
        self.yellow_green19 = ColorScheme(
            name='yellow_green19',
            colors=['#BFD30F','#060018','#C20C19','#FA845C','#F5DD95'],
            harmony='other'
        )
        
        self.yellow_green20 = ColorScheme(
            name='yellow_green20',
            colors=['#BAC654','#30958B','#690F4D','#090419','#C24813'],
            harmony='other'
        )
        
        self.yellow_green21 = ColorScheme(
            name='yellow_green21',
            colors=['#7C60A1','#5F999E','#C6CC9F','#FA9996','#CD7DA7'],
            harmony='other'
        )
        
        # page 102
        self.yellow_green22 = ColorScheme(
            name='yellow_green22',
            colors=['#9900FF','#A640BF','#B38080','#BFBF40','#CCFF00'],
            harmony='other'
        )
        
        self.yellow_green23 = ColorScheme(
            name='yellow_green23',
            colors=['#551BB3','#268FBE','#2CB8B2','#3DDB8F','#A9F04D'],
            harmony='other'
        )
        
        self.yellow_green24 = ColorScheme(
            name='yellow_green24',
            colors=['#42393B','#75C9A3','#BAC99A','#FFC897','#F7EFA2'],
            harmony='other'
        )
        
        self.yellow_green25 = ColorScheme(
            name='yellow_green25',
            colors=['#442C46','#3E4F56','#377165','#6A9041','#9CAE1C'],
            harmony='other'
        )
        
        self.yellow_green26 = ColorScheme(
            name='yellow_green26',
            colors=['#9E9674','#79B79D','#9FCCA0','#C6E2A2','#ECF7A5'],
            harmony='other'
        )
        
        self.yellow_green27 = ColorScheme(
            name='yellow_green27',
            colors=['#80B358','#969932','#8F6842','#85424D','#634653'],
            harmony='other'
        )
        
        self.yellow_green28 = ColorScheme(
            name='yellow_green28',
            colors=['#FFFF00','#CCD91A','#99B333','#668C4D','#336666'],
            harmony='other'
        )

        # page 104
        self.green1 = ColorScheme(
            name='green1',
            colors=['#93B314','#418F15','#057418','#025A1B','#03361C'],
            harmony='monochromatic'
        )

        self.green2 = ColorScheme(
            name='green2',
            colors=['#FDFEF5','#ECF8E9','#D3FDBD','#82BB63','#123D12'],
            harmony='monochromatic'
        )

        self.green3 = ColorScheme(
            name='green3',
            colors=['#003030','#186030','#489048','#60C048','#A8F090'],
            harmony='monochromatic'
        )

        # page 105
        self.green4 = ColorScheme(
            name='green4',
            colors=['#27471F','#5B8551','#7EB870','#AFFF9C','#C7E8BE'],
            harmony='monochromatic'
        )

        # page 106
        self.green5 = ColorScheme(
            name='green5',
            colors=['#FAF8BE','#F7F38D','#E9E56E','#BDE96E','#67D392'],
            harmony='analogous'
        )

        self.green6 = ColorScheme(
            name='green6',
            colors=['#C2B248','#8FC244','#6AC45A','#4AB57A','#39A38C'],
            harmony='analogous'
        )

        self.green7 = ColorScheme(
            name='green7',
            colors=['#27471F','#5B8551','#7EB870','#AFFF9C','#C7E8BE'],
            harmony='analogous'
        )

        # page 107
        self.green8 = ColorScheme(
            name='green8',
            colors=['#487352','#609169','#82A36D','#C4B970','#EDCB74'],
            harmony='analogous'
        )

        self.green9 = ColorScheme(
            name='green9',
            colors=['#1B676B','#519548','#88C425','#BEF202','#EAFDE6'],
            harmony='analogous'
        )

        # page 108
        self.green10 = ColorScheme(
            name='green10',
            colors=['#DCA858','#A57C68','#6E5078','#709D95','#72EAB2'],
            harmony='triadic'
        )

        # page 109
        self.green11 = ColorScheme(
            name='green11',
            colors=['#86D661','#61A840','#F3E19A','#F89E54','#A046B3'],
            harmony='triadic'
        )

        # page 110
        self.green12 = ColorScheme(
            name='green12',
            colors=['#58817B','#B8E7CB','#EDFFD1','#FFCEB9','#885A78'],
            harmony='split-complementary'
        )

        self.green13 = ColorScheme(
            name='green13',
            colors=['#C6D6D5','#79BA7C','#8B8F29','#854424','#7A104C'],
            harmony='split-complementary'
        )

        # page 111
        self.green14 = ColorScheme(
            name='green14',
            colors=['#CC4C28','#994646','#7A4259','#70596B','#708C7F'],
            harmony='split-complementary'
        )

        self.green15 = ColorScheme(
            name='green15',
            colors=['#516755','#522934','#A51600','#B84230','#C88D63'],
            harmony='split-complementary'
        )

        self.green16 = ColorScheme(
            name='green16',
            colors=['#9EFF78','#93C76A','#898E5C','#7E564D','#731D3F'],
            harmony='split-complementary'
        )

        self.green17 = ColorScheme(
            name='green17',
            colors=['#801C57','#BE786E','#FBD385','#92A951','#287E1C'],
            harmony='split-complementary'
        )

        # page 112
        self.green18 = ColorScheme(
            name='green18',
            colors=['#C4AD47','#94923A','#8C8011','#8C3B12','#700C0C'],
            harmony='complementary'
        )

        self.green19 = ColorScheme(
            name='green19',
            colors=['#4B806C','#61AF92','#D7E7B9','#AF6162','#804B4C'],
            harmony='complementary'
        )

        # page 113
        self.green20 = ColorScheme(
            name='green20',
            colors=['#FFA8A8','#FFDBDB','#FFFFFF','#D7FFBD','#A3EB73'],
            harmony='complementary'
        )

        self.green21 = ColorScheme(
            name='green21',
            colors=['#4AA554','#5D925C','#6F7F64','#826C6C','#C06666'],
            harmony='complementary'
        )

        # page 114
        self.green22 = ColorScheme(
            name='green22',
            colors=['#535555','#5E9C54','#B2CA52','#F5D899','#EE7D61'],
            harmony='other'
        )

        self.green23 = ColorScheme(
            name='green23',
            colors=['#E58300','#FFD463','#D7FFC5','#8DBD8A','#57B027'],
            harmony='other'
        )

        self.green24 = ColorScheme(
            name='green24',
            colors=['#574B5A','#717571','#8BA088','#A5CB9F','#BFF6B6'],
            harmony='other'
        )

        self.green25 = ColorScheme(
            name='green25',
            colors=['#CEF617','#93DA5C','#66C68E','#37B0C4','#17A1E9'],
            harmony='other'
        )

        self.green26 = ColorScheme(
            name='green26',
            colors=['#3D9166','#B8D156','#EDE291','#D19E30','#8C451F'],
            harmony='other'
        )

        self.green27 = ColorScheme(
            name='green27',
            colors=['#FFF6A8','#C4F299','#83D698','#55AB98','#5B6B68'],
            harmony='other'
        )

        self.green28 = ColorScheme(
            name='green28',
            colors=['#355C5E','#3D785A','#9C8B41','#DE8C59','#E35465'],
            harmony='other'
        )

        # page 115
        self.green29 = ColorScheme(
            name='green29',
            colors=['#420205','#5F4D54','#717355','#87A36E','#83D488'],
            harmony='other'
        )

        self.green30 = ColorScheme(
            name='green30',
            colors=['#E8F255','#C0DD2B','#84C660','#49B096','#867AA1'],
            harmony='other'
        )

        self.green31 = ColorScheme(
            name='green31',
            colors=['#2FFEF6','#C0DD2B','#84C660','#49B096','#867AA1'],
            harmony='other'
        )

        self.green32 = ColorScheme(
            name='green32',
            colors=['#1C120A','#699124','#90AD87','#BDD1AE','#E2E8D5'],
            harmony='other'
        )

        # page 117
        self.green_blue1 = ColorScheme(
            name='green_blue1',
            colors=['#F7FEFF','#CEF2F0','#83CCBC','#47B39F','#208185'],
            harmony='monochromatic'
        )

        self.green_blue2 = ColorScheme(
            name='green_blue2',
            colors=['#CFFFF1','#95CCC4','#008683','#415B5E','#BBE7D6'],
            harmony='monochromatic'
        )
        
        self.green_blue3 = ColorScheme(
            name='green_blue3',
            colors=['#D5EBE8','#A9D9D4','#8AC2BC','#6DADA7','#4A918A'],
            harmony='monochromatic'
        )

        # page 118
        self.green_blue4 = ColorScheme(
            name='green_blue4',
            colors=['#DDFFCC','#7EC9AB','#008A84','#006D68','#005753'],
            harmony='monochromatic'
        )

        self.green_blue5 = ColorScheme(
            name='green_blue5',
            colors=['#435452','#6F9F99','#C1DBD6','#F3F8F7'],
            harmony='monochromatic'
        )

        self.green_blue6 = ColorScheme(
            name='green_blue6',
            colors=['#005863','#086970','#21AEB8','#4AD4D1','#77FCEF'],
            harmony='monochromatic'
        )

        self.green_blue7 = ColorScheme(
            name='green_blue7',
            colors=['#27E1F2','#66E7F2','#A5ECF2','#CDF5F7','#FFFFFF'],
            harmony='monochromatic'
        )

        # page 119
        self.green_blue8 = ColorScheme(
            name='green_blue8',
            colors=['#242A42','#2B747A','#569A81','#9CDE96','#C3FDB0'],
            harmony='analogous'
        )

        self.green_blue9 = ColorScheme(
            name='green_blue9',
            colors=['#0BB4D5','#46C2C4','#81CFB2','#AAD2BA','#D2D5C2'],
            harmony='analogous'
        )

        self.green_blue10 = ColorScheme(
            name='green_blue10',
            colors=['#3D6B5A','#548F7F','#6BB3A4','#82D7C8','#99FBED'],
            harmony='analogous'
        )

        self.green_blue11 = ColorScheme(
            name='green_blue11',
            colors=['#00747D','#719D9C','#AFD0AC','#E6F8BA','#298879'],
            harmony='analogous'
        )

        # page 120 
        self.green_blue12 = ColorScheme(
            name='green_blue12',
            colors=['#95D1CC','#2F978F','#166D66','#D3DA90','#EDF1BE'],
            harmony='analogous'
        )

        self.green_blue13 = ColorScheme(
            name='green_blue13',
            colors=['#166665','#468C77','#97B88D','#DCE3A6','#D1B254'],
            harmony='analogous'
        )

        self.green_blue14 = ColorScheme(
            name='green_blue14',
            colors=['#3D3843','#3C7182','#59C2A9','#8EDB86','#C2ED62'],
            harmony='analogous'
        )

        self.green_blue15 = ColorScheme(
            name='green_blue15',
            colors=['#939C7D','#58786B','#32555D','#44344C','#44193B'],
            harmony='analogous'
        )

        # page 121
        self.green_blue16 = ColorScheme(
            name='green_blue16',
            colors=['#952F67','#FCF2B1','#CBD6A0','#77B88D','#528278'],
            harmony='triadic'
        )

        self.green_blue17 = ColorScheme(
            name='green_blue17',
            colors=['#86B7BA','#D9D3BA','#FABD7F','#FA8A7F','#ED095D'],
            harmony='triadic'
        )

        self.green_blue17 = ColorScheme(
            name='green_blue17',
            colors=['#633651','#3B8B92','#72BD94','#FEECA9','#FFFBC3'],
            harmony='triadic'
        )

        self.green_blue18 = ColorScheme(
            name='green_blue18',
            colors=['#FFAC66','#FBE7A9','#97DBBF','#2FADA6','#7E4D6E'],
            harmony='triadic'
        )

        self.green_blue19 = ColorScheme(
            name='green_blue19',
            colors=['#EBEAAE','#EEC852','#77A57F','#3A8075','#512E4C'],
            harmony='triadic'
        )

        # page 122
        self.green_blue20 = ColorScheme(
            name='green_blue20',
            colors=['#F1C75C','#448683','#185352','#6F142E','#AB0031'],
            harmony='triadic'
        )

        self.green_blue21 = ColorScheme(
            name='green_blue21',
            colors=['#CDE9CA','#2E928F','#471B2D','#FFF1D1','#FCD38B'],
            harmony='triadic'
        )

        self.green_blue22 = ColorScheme(
            name='green_blue22',
            colors=['#59917A','#1C6958','#6F9E9D','#CCBCC9','#EFDDA1'],
            harmony='triadic'
        )

        self.green_blue23 = ColorScheme(
            name='green_blue23',
            colors=['#245F81','#2EABB6','#81CFD6','#F1C823','#C9336F'],
            harmony='triadic'
        )

        self.green_blue24 = ColorScheme(
            name='green_blue24',
            colors=['#4E0B49','#2E685C','#81C0A4','#E7A645','#FAE164'],
            harmony='triadic'
        )

        # page 123
        self.green_blue25 = ColorScheme(
            name='green_blue25',
            colors=['#59ADB3','#408A7D','#1C6B6E','#DE7D1D','#E00B2F'],
            harmony='split-complementary'
        )

        self.green_blue26 = ColorScheme(
            name='green_blue26',
            colors=['#E8E2AE','#FFAD2D','#36A8A6','#6F736E','#8C5A5E'],
            harmony='split-complementary'
        )

        self.green_blue27 = ColorScheme(
            name='green_blue27',
            colors=['#4E6062','#189E7B','#63BF72','#FAB75E','#FA5D5B'],
            harmony='split-complementary'
        )

        # page 124
        self.green_blue28 = ColorScheme(
            name='green_blue28',
            colors=['#006060','#187860','#D8C090','#C09060','#D84848'],
            harmony='split-complementary'
        )

        self.green_blue29 = ColorScheme(
            name='green_blue29',
            colors=['#F7EEC4','#F8C793','#FF8175','#28776E','#136850'],
            harmony='split-complementary'
        )

        self.green_blue30 = ColorScheme(
            name='green_blue30',
            colors=['#73A3A3','#316F6F','#2E4242','#D32323','#F1963C'],
            harmony='split-complementary'
        )

        # page 125
        self.green_blue31 = ColorScheme(
            name='green_blue31',
            colors=['#2E3E73','#008895','#89CCB8','#F9F5DA','#F56F42'],
            harmony='complementary'
        )

        # page 127 
        self.green_blue32 = ColorScheme(
            name='green_blue32',
            colors=['#61C289','#B6C261','#FFCB30','#FFDE7D','#77D4C7'],
            harmony='other'
        )

        self.green_blue32 = ColorScheme(
            name='green_blue32',
            colors=['#C9B7BC','#7E6F92','#4D6B7A','#00A8A8','#B0D6D0'],
            harmony='other'
        )

        self.green_blue33 = ColorScheme(
            name='green_blue33',
            colors=['#FFCC33','#E6D966','#CCE699','#B3F2CC','#99FFFF'],
            harmony='other'
        )

        self.green_blue34 = ColorScheme(
            name='green_blue34',
            colors=['#DAEADC','#316E68','#46263B','#E64343','#F1B244'],
            harmony='other'
        )

        # page 128
        self.green_blue35 = ColorScheme(
            name='green_blue35',
            colors=['#3B8A81','#7C9A71','#DEAD59','#DE8F59','#203131'],
            harmony='other'
        )  

        self.green_blue36 = ColorScheme(
            name='green_blue36',
            colors=['#DB6E2A','#DEBE31','#919922','#22996B','#042833'],
            harmony='other'
        )  

        self.green_blue37 = ColorScheme(
            name='green_blue37',
            colors=['#0C4C4C','#548E7A','#BAC090','#F9E09D','#752720'],
            harmony='other'
        )  
        
        # page 130
        self.blue1 = ColorScheme(
            name='blue1',
            colors=['#B0E5FB','#63AFD5','#337BB1','#175389','#05366A'],
            harmony='monochromatic'
        )

        self.blue2 = ColorScheme(
            name='blue2',
            colors=['#006699','#2A70AE','#5486BB','#99BBDD','#D4E8F7'],
            harmony='monochromatic'
        )

        self.blue3 = ColorScheme(
            name='blue3',
            colors=['#EEF2F6','#CCE4FB','#B2D5F8','#91C2F3','#75B3F0'],
            harmony='monochromatic'
        )

        # page 131
        self.blue4 = ColorScheme(
            name='blue4',
            colors=['#29405A','#395A7E','#4974A2','#658EB9','#ACC2D9'],
            harmony='monochromatic'
        )

        # page 132
        self.blue5 = ColorScheme(
            name='blue5',
            colors=['#69C9BF','#5CB5B9','#6392AB','#656E8D','#4D5778'],
            harmony='analogous'
        )

        self.blue6 = ColorScheme(
            name='blue6',
            colors=['#D3E2B6','#C3DBB4','#AACCB1','#87BDB1','#68B3AF'],
            harmony='analogous'
        )

        self.blue7 = ColorScheme(
            name='blue7',
            colors=['#A98682','#957D8A','#7D7D9F','#5986C7','#0079FC'],
            harmony='analogous'
        )

        # page 133
        self.blue8 = ColorScheme(
            name='blue8',
            colors=['#C2E6CA','#8DB39C','#6473AE','#364190','#3346A4'],
            harmony='analogous'
        )

        self.blue9 = ColorScheme(
            name='blue9',
            colors=['#5BC7D4','#059185','#1A4C6C','#053054','#071C39'],
            harmony='analogous'
        )

        self.blue10 = ColorScheme(
            name='blue10',
            colors=['#F2EDDF','#61C2C0','#6161C2','#194F73','#04042B'],
            harmony='analogous'
        )

        # page 134
        self.blue11 = ColorScheme(
            name='blue11',
            colors=['#073C90','#5F70D8','#F84765','#F9AF08','#E5E940'],
            harmony='triadic'
        )

        self.blue12 = ColorScheme(
            name='blue12',
            colors=['#FFFCA9','#CC3D03','#8C223B','#4A1865','#2E3E81'],
            harmony='triadic'
        )

        # page 135
        self.blue13 = ColorScheme(
            name='blue13',
            colors=['#677E9C','#9DA68D','#E1D772','#FAF889','#9E1205'],
            harmony='triadic'
        )

        self.blue14 = ColorScheme(
            name='blue14',
            colors=['#15214C','#006C79','#F7E321','#F8F898','#C5372A'],
            harmony='triadic'
        )

        # page 136
        self.blue15 = ColorScheme(
            name='blue15',
            colors=['#414980','#9E5D62','#C76555','#C7A051','#C7CD4F'],
            harmony='split-complementary'
        )

        # page 137
        self.blue16 = ColorScheme(
            name='blue16',
            colors=['#FC8A58','#FFCF40','#006569','#005069','#003369'],
            harmony='split-complementary'
        )

        self.blue17 = ColorScheme(
            name='blue17',
            colors=['#A8D8F0','#78C0F0','#4890C0','#FF8F57','#FFCD57'],
            harmony='split-complementary'
        )

        # page 138
        self.blue18 = ColorScheme(
            name='blue18',
            colors=['#2064F7','#34ABEB','#6FC4FC','#FF943D','#FFB67A'],
            harmony='complementary'
        )

        # page 139
        self.blue19 = ColorScheme(
            name='blue19',
            colors=['#00154A','#002F59','#6B6159','#F9A516','#FFBA5F'],
            harmony='complementary'
        )

        self.blue20 = ColorScheme(
            name='blue20',
            colors=['#344F6D','#4B5D71','#787977','#B49673','#FFA964'],
            harmony='complementary'
        )

        self.blue21 = ColorScheme(
            name='blue21',
            colors=['#8CBFF2','#A6BFD9','#BFBFBF','#D9BFA6','#F2BF8C'],
            harmony='complementary'
        )

        # page 140
        self.blue22 = ColorScheme(
            name='blue22',
            colors=['#97DBC4','#A3BDDE','#BF7ECE','#6A2C7F','#264283'],
            harmony='other'
        )

        self.blue23 = ColorScheme(
            name='blue23',
            colors=['#243A61','#4D4885','#80507E','#B34F7A','#E03F44'],
            harmony='other'
        )

        self.blue24 = ColorScheme(
            name='blue24',
            colors=['#F8FFEB','#B1C7DE','#486380','#175282','#8C1B1B'],
            harmony='other'
        )

        self.blue25 = ColorScheme(
            name='blue25',
            colors=['#4A4D85','#ECFEFE','#FAD9FA','#A2C1FA','#792DD6'],
            harmony='other'
        )

        # page 141
        self.blue26 = ColorScheme(
            name='blue26',
            colors=['#D2EB63','#7E9177','#607294','#516399','#4D3378'],
            harmony='other'
        )

        self.blue27 = ColorScheme(
            name='blue27',
            colors=['#3D3C59','#3C729C','#D2E2E3','#FFFFF5','#886C5F'],
            harmony='other'
        )

        self.blue28 = ColorScheme(
            name='blue28',
            colors=['#67DBEB','#CAE2FC','#E7FCCA','#FCF6CA','#D7F23D'],
            harmony='other'
        )

        # page 143
        self.blue_violet1 = ColorScheme(
            name='blue_violet1',
            colors=['#5D14F8','#8C5AF7','#C0A5F8','#E5DCFA','#F2F0F7'],
            harmony='monochromatic'
        )

        self.blue_violet2 = ColorScheme(
            name='blue_violet2',
            colors=['#6643E6','#967DF0','#B3A4EB','#D2CCEB','#EEEAF2'],
            harmony='monochromatic'
        )

        # page 144
        self.blue_violet3 = ColorScheme(
            name='blue_violet3',
            colors=['#EAE6F7','#D8CDF7','#A28DE3','#4E28BF','#250680'],
            harmony='monochromatic'
        )

        # page 145
        self.blue_violet4 = ColorScheme(
            name='blue_violet4',
            colors=['#CA549E','#EC684F','#9177B4','#F6B35A','#7180B7'],
            harmony='analogous'
        )

        # page 146
        self.blue_violet5 = ColorScheme(
            name='blue_violet5',
            colors=['#E3F7F6','#90CEBC','#6E62A3','#363050','#120F20'],
            harmony='analogous'
        )

        self.blue_violet6 = ColorScheme(
            name='blue_violet6',
            colors=['#3E2DA8','#4837B8','#6136C7','#7B3EB8','#BD46B5'],
            harmony='analogous'
        )

        # page 147
        self.blue_violet7 = ColorScheme(
            name='blue_violet7',
            colors=['#898599','#545861','#323938','#D48070','#F2FECE'],
            harmony='triadic'
        )

        # page 148
        self.blue_violet7 = ColorScheme(
            name='blue_violet7',
            colors=['#898599','#545861','#323938','#D48070','#F2FECE'],
            harmony='triadic'
        )

        # page 149
        self.blue_violet8 = ColorScheme(
            name='blue_violet8',
            colors=['#923DDB','#542CB0','#FFB254','#E0D800','#F5E900'],
            harmony='split-complementary'
        )

        self.blue_violet9 = ColorScheme(
            name='blue_violet9',
            colors=['#D3CBFD','#B0B3FC','#C0BCB6','#FFC67C','#FFFF68'],
            harmony='split-complementary'
        )

        # page 150
        self.blue_violet10 = ColorScheme(
            name='blue_violet10',
            colors=['#BBA5E6','#F0EEA5','#FCC792','#E8A9DF','#F9FAF7'],
            harmony='split-complementary'
        )

        self.blue_violet11 = ColorScheme(
            name='blue_violet11',
            colors=['#FCF9E3','#FFFAC7','#FCE4BF','#A9A5C5','#8C7EAC'],
            harmony='split-complementary'
        )

        self.blue_violet12 = ColorScheme(
            name='blue_violet12',
            colors=['#F7F4B7','#F7E38B','#FFB987','#554A75','#332A91'],
            harmony='split-complementary'
        )

        self.blue_violet13 = ColorScheme(
            name='blue_violet13',
            colors=['#9D90C6','#5051A3','#56381E','#FFB452','#FFFFBF'],
            harmony='split-complementary'
        )

        # page 151
        self.blue_violet14 = ColorScheme(
            name='blue_violet14',
            colors=['#FCB956','#FCD456','#FDEEBA','#CFBAFD','#340F83'],
            harmony='complementary'
        )

        self.blue_violet15 = ColorScheme(
            name='blue_violet15',
            colors=['#563D91','#8365BF','#9090C0','#F3E9AC','#D0BE74'],
            harmony='complementary'
        )

        # page 152
        self.blue_violet16 = ColorScheme(
            name='blue_violet16',
            colors=['#1B1336','#37286B','#835FFD','#FFC259','#FFDEA5'],
            harmony='complementary'
        )

        # page 153
        self.blue_violet17 = ColorScheme(
            name='blue_violet17',
            colors=['#857C33','#915552','#A66279','#B385C9','#B3B3FE'],
            harmony='other'
        )

        self.blue_violet18 = ColorScheme(
            name='blue_violet18',
            colors=['#BFA499','#999999','#5F9299','#5F7199','#523D91'],
            harmony='other'
        )

        self.blue_violet19 = ColorScheme(
            name='blue_violet19',
            colors=['#736295','#6D8D9F','#91C2B1','#D9D8AF','#ED966A'],
            harmony='other'
        )

        self.blue_violet20 = ColorScheme(
            name='blue_violet20',
            colors=['#403867','#4D7471','#FED5A9','#F7A983','#FD6864'],
            harmony='other'
        )

        self.blue_violet21 = ColorScheme(
            name='blue_violet21',
            colors=['#CFB12B','#C7EDCA','#6DCCA5','#185466','#211154'],
            harmony='other'
        )

        self.blue_violet22 = ColorScheme(
            name='blue_violet22',
            colors=['#100061','#75003C','#F79C1B','#C43911','#4A1461'],
            harmony='other'
        )

        # page 154
        self.blue_violet23 = ColorScheme(
            name='blue_violet23',
            colors=['#C17CDE','#B19DEB','#9DE5EB','#EBE99D','#EB9DBF'],
            harmony='other'
        )

        self.blue_violet24 = ColorScheme(
            name='blue_violet24',
            colors=['#534296','#7668AC','#89A1C5','#B1DAC3','#F1F5C2'],
            harmony='other'
        )

        self.blue_violet25 = ColorScheme(
            name='blue_violet25',
            colors=['#E8C47B','#FF8482','#87709E','#58537B','#063853'],
            harmony='other'
        )

        self.blue_violet26 = ColorScheme(
            name='blue_violet26',
            colors=['#3200A6','#8800FF','#FF8000','#FF4000','#FF0090'],
            harmony='other'
        )

        # page 156
        self.violet1 = ColorScheme(
            name='violet1',
            colors=['#8B57A8','#A379BA','#BB9BCC','#D2BDDE','#E9DFEF'],
            harmony='monochromatic'
        )

        # page 157
        self.violet2 = ColorScheme(
            name='violet2',
            colors=['#3B2446','#583768','#815197','#B06FCE','#EAC4FC'],
            harmony='monochromatic'
        )

        # page 158
        self.violet3 = ColorScheme(
            name='violet3',
            colors=['#FFC361','#CC6C51','#8F1148','#592831','#543E3E'],
            harmony='analogous'
        )

        self.violet4 = ColorScheme(
            name='violet4',
            colors=['#CCFFFF','#CCBFFF','#CC80FF','#CC40FF','#CC00FF'],
            harmony='analogous'
        )

        # page 159
        self.violet5 = ColorScheme(
            name='violet5',
            colors=['#3300FF','#6600FF','#9900FF','#CC00FF','#FF00FF'],
            harmony='analogous'
        )

        self.violet6 = ColorScheme(
            name='violet6',
            colors=['#88005C','#6B1B66','#531B6B','#3F1B6B','#2D0E5E'],
            harmony='analogous'
        )

        self.violet7 = ColorScheme(
            name='violet7',
            colors=['#CCFFCC','#BBCCBB','#A39AAB','#7B5E8C','#3D1C66'],
            harmony='analogous'
        )

        # page 160
        self.violet8 = ColorScheme(
            name='violet8',
            colors=['#D9C991','#CCA78C','#72877F','#4F6C7A','#877D8C'],
            harmony='triadic'
        )

        self.violet9 = ColorScheme(
            name='violet9',
            colors=['#88B5A6','#70727D','#541482','#940076','#FCBD88'],
            harmony='triadic'
        )

        self.violet10 = ColorScheme(
            name='violet10',
            colors=['#F8A14C','#CC7783','#A14DB9','#7786AF','#4AC2A4'],
            harmony='triadic'
        )

        # page 161
        self.violet11 = ColorScheme(
            name='violet11',
            colors=['#094137','#267556','#EEA538','#403155','#9B1C5D'],
            harmony='triadic'
        )

        self.violet12 = ColorScheme(
            name='violet12',
            colors=['#336633','#669966','#FAEBD7','#996699','#330066'],
            harmony='triadic'
        )

        self.violet13 = ColorScheme(
            name='violet13',
            colors=['#2C8A75','#00707B','#502B5F','#FBB36B','#FDDDD0'],
            harmony='triadic'
        )

        # page 162
        self.violet14 = ColorScheme(
            name='violet14',
            colors=['#FFE6B5','#FFD278','#CEFF85','#E894FF','#EEB8FF'],
            harmony='split-complementary'
        )

        self.violet15 = ColorScheme(
            name='violet15',
            colors=['#5E7422','#939477','#C9B5CD','#DECEC7','#F4E8C0'],
            harmony='split-complementary'
        )

        # page 163
        self.violet16 = ColorScheme(
            name='violet16',
            colors=['#304800','#789048','#CFBC84','#946892','#6E5475'],
            harmony='split-complementary'
        )

        self.violet17 = ColorScheme(
            name='violet17',
            colors=['#35254F','#6E475D','#AB8D78','#B3A66D','#ADBD39'],
            harmony='split-complementary'
        )

        # page 165
        self.violet18 = ColorScheme(
            name='violet18',
            colors=['#6F5E85','#827099','#99969E','#ABAA84','#E3E162'],
            harmony='complementary'
        )

        self.violet19 = ColorScheme(
            name='violet19',
            colors=['#DFDF3E','#C0C058','#AA8181','#914AA3','#8427A0'],
            harmony='complementary'
        )

        # page 166
        self.violet20 = ColorScheme(
            name='violet20',
            colors=['#742487','#EB2B81','#FCB259','#FFF79A','#00ADB3'],
            harmony='other'
        )

        self.violet21 = ColorScheme(
            name='violet21',
            colors=['#F2D785','#BA7B75','#8C3C56','#571B53','#200E38'],
            harmony='other'
        )

        self.violet22 = ColorScheme(
            name='violet22',
            colors=['#F7D3C7','#FC8F79','#C25771','#842060','#AF78C5'],
            harmony='other'
        )

        self.violet23 = ColorScheme(
            name='violet23',
            colors=['#0F9987','#5D8B9C','#7C93CC','#ADA2F2','#E999FF'],
            harmony='other'
        )

        self.violet24 = ColorScheme(
            name='violet24',
            colors=['#B460F0','#C776D0','#DA8CB0','#EDA290','#FFB870'],
            harmony='other'
        )

        self.violet25 = ColorScheme(
            name='violet25',
            colors=['#644A6B','#808C96','#B7D1A7','#E1EBAB','#F9FFA1'],
            harmony='other'
        )

        self.violet26 = ColorScheme(
            name='violet26',
            colors=['#620082','#4F5880','#8C6282','#FF914D','#FFAE00'],
            harmony='other'
        )

        # page 167
        self.violet27 = ColorScheme(
            name='violet27',
            colors=['#796A7F','#A4ADA8','#E4BEA9','#FAD4A7','#E87C7C'],
            harmony='other'
        )

        self.violet28 = ColorScheme(
            name='violet28',
            colors=['#726178','#A17071','#D4786B','#DBAF73','#DECA9C'],
            harmony='other'
        )

        self.violet29 = ColorScheme(
            name='violet29',
            colors=['#662578','#58428A','#428A78','#C2D4AB','#FFFAC9'],
            harmony='other'
        )

        self.violet30 = ColorScheme(
            name='violet30',
            colors=['#E1F56B','#F0AF6D','#FF695D','#D90D6A','#2D1553'],
            harmony='other'
        )

        self.violet31 = ColorScheme(
            name='violet31',
            colors=['#F7925C','#6F1E4A','#2E1149','#00224C','#2B5563'],
            harmony='other'
        )

        self.violet32 = ColorScheme(
            name='violet32',
            colors=['#E58227','#FFB443','#882B33','#602042','#6C267C'],
            harmony='other'
        )

        self.violet33 = ColorScheme(
            name='violet33',
            colors=['#EDC0A9','#CCB0E0','#F8E193','#CCE0AF','#87AAC0'],
            harmony='other'
        )

        self.violet34 = ColorScheme(
            name='violet34',
            colors=['#F7C94F','#B4A76A','#728686','#56436E','#3A0157'],
            harmony='other'
        )

        # page 169
        self.violet_red1 = ColorScheme(
            name='violet_red1',
            colors=['#FF5A98','#FF0273','#D2004F','#9B0034','#750029'],
            harmony='monochromatic'
        )

        self.violet_red2 = ColorScheme(
            name='violet_red2',
            colors=['#25303F','#57213E','#99124D','#CC044C','#FD054B'],
            harmony='monochromatic'
        )

        self.violet_red3 = ColorScheme(
            name='violet_red3',
            colors=['#99316F','#AA5F8C','#C2A7C0','#C8CFCC','#D3DDD5'],
            harmony='monochromatic'
        )

        # page 170
        self.violet_red4 = ColorScheme(
            name='violet_red4',
            colors=['#99316F','#AA5F8C','#C2A7C0','#C8CFCC','#D3DDD5'],
            harmony='monochromatic'
        )

        self.violet_red5 = ColorScheme(
            name='violet_red5',
            colors=['#FAE7FB','#FAD1F3','#F9C0ED','#F2A1E4','#EE95E7'],
            harmony='monochromatic'
        )

        self.violet_red6 = ColorScheme(
            name='violet_red6',
            colors=['#3D021A','#72193D','#9E3C63','#CA7497','#F5CFDE'],
            harmony='monochromatic'
        )

        # page 171
        self.violet_red7 = ColorScheme(
            name='violet_red7',
            colors=['#FF2636','#FA8611','#ECAC5F','#DED2AD','#CF2166'],
            harmony='analogous'
        )

        self.violet_red8 = ColorScheme(
            name='violet_red8',
            colors=['#35254C','#5D2A57','#862E62','#B52E6D','#EE2B79'],
            harmony='analogous'
        )

        self.violet_red9 = ColorScheme(
            name='violet_red9',
            colors=['#35254C','#5D2A57','#862E62','#B52E6D','#EE2B79'],
            harmony='analogous'
        )

        # page 172
        self.violet_red10 = ColorScheme(
            name='violet_red10',
            colors=['#260420','#3D1734','#7B475E','#CA99AE','#F1D6D2'],
            harmony='analogous'
        )

        self.violet_red11 = ColorScheme(
            name='violet_red11',
            colors=['#D6A372','#D1696B','#CE005F','#9A0054','#80004A'],
            harmony='analogous'
        )

        self.violet_red12 = ColorScheme(
            name='violet_red12',
            colors=['#D6A372','#D1696B','#CE005F','#9A0054','#80004A'],
            harmony='analogous'
        )

        self.violet_red13 = ColorScheme(
            name='violet_red13',
            colors=['#D7ADDB','#A783C7','#8C3C83','#69005C','#501457'],
            harmony='analogous'
        )

        self.violet_red14 = ColorScheme(
            name='violet_red14',
            colors=['#FCB3EE','#ED66D2','#B80093','#702A6E','#120014'],
            harmony='analogous'
        )

        self.violet_red15 = ColorScheme(
            name='violet_red15',
            colors=['#E73155','#C72559','#A7195E','#860C62','#670067'],
            harmony='analogous'
        )

        self.violet_red16 = ColorScheme(
            name='violet_red16',
            colors=['#AC1E55','#AC1E77','#AC1E99','#A42FE0','#A543F4'],
            harmony='analogous'
        )

        self.violet_red17 = ColorScheme(
            name='violet_red17',
            colors=['#010F70','#451D88','#8F2988','#C43784','#EA1866'],
            harmony='analogous'
        )

        self.violet_red18 = ColorScheme(
            name='violet_red18',
            colors=['#FE7566','#E96375','#D7336C','#C42172','#AC3971'],
            harmony='analogous'
        )

        # page 173
        self.violet_red19 = ColorScheme(
            name='violet_red19',
            colors=['#013E8A','#FCF988','#FED46F','#B92F49','#85274B'],
            harmony='triadic'
        )

        self.violet_red20 = ColorScheme(
            name='violet_red20',
            colors=['#937383','#5A3248','#307383','#93BD9A','#FED86B'],
            harmony='triadic'
        )

        self.violet_red21 = ColorScheme(
            name='violet_red21',
            colors=['#288580','#FFEEBD','#F2A38D','#E03D6B','#85666F'],
            harmony='triadic'
        )

        # page 174
        self.violet_red22 = ColorScheme(
            name='violet_red22',
            colors=['#E3D394','#ACAC95','#899497','#9C798B','#BC4F79'],
            harmony='triadic'
        )

        self.violet_red23 = ColorScheme(
            name='violet_red23',
            colors=['#912C54','#B5867D','#A3BFA3','#CED9B2','#FFF5CF'],
            harmony='triadic'
        )

        self.violet_red24 = ColorScheme(
            name='violet_red24',
            colors=['#FAE4A6','#BACAA7','#76B2A8','#736D7A','#702A4B'],
            harmony='triadic'
        )

        self.violet_red25 = ColorScheme(
            name='violet_red25',
            colors=['#FCE8BD','#8FC4AA','#328094','#75414F','#BF5271'],
            harmony='triadic'
        )

        # page 175
        self.violet_red26 = ColorScheme(
            name='violet_red26',
            colors=['#846F7F','#C697BB','#B1D9B0','#E7FFC1','#FFFDC1'],
            harmony='split-complementary'
        )

        self.violet_red27 = ColorScheme(
            name='violet_red27',
            colors=['#700031','#9E1B4B','#EBE86A','#79BA5B','#5BA152'],
            harmony='split-complementary'
        )

        # page 176
        self.violet_red28 = ColorScheme(
            name='violet_red28',
            colors=['#FDFBD2','#B4E2B4','#75A48B','#7C526A','#870D32'],
            harmony='split-complementary'
        )

        self.violet_red29 = ColorScheme(
            name='violet_red29',
            colors=['#F5F8A5','#738F7B','#6D152E','#AA1B38','#CE3050'],
            harmony='split-complementary'
        )

        # page 177
        self.violet_red30 = ColorScheme(
            name='violet_red30',
            colors=['#C1E78E','#C6B185','#94716E','#70545F','#4A353E'],
            harmony='complementary'
        )

        self.violet_red31 = ColorScheme(
            name='violet_red31',
            colors=['#ECFFA5','#BAC78D','#AC4343','#75112D','#551E2E'],
            harmony='complementary'
        )

        self.violet_red32 = ColorScheme(
            name='violet_red32',
            colors=['#8D5063','#5F2B2B','#A83B59','#B5CC9D','#F7FFD8'],
            harmony='complementary'
        )

        # page 178
        self.violet_red33 = ColorScheme(
            name='violet_red33',
            colors=['#382843','#702D53','#AB276B','#BBC4B3','#DDE0C8'],
            harmony='complementary'
        )

        # page 179
        self.violet_red34 = ColorScheme(
            name='violet_red34',
            colors=['#8FC9B9','#D8D9C0','#D18E8F','#AB5C72','#91334F'],
            harmony='other'
        )

        self.violet_red35 = ColorScheme(
            name='violet_red35',
            colors=['#C40037','#F18B00','#5E0057','#FDFFD9','#CB007F'],
            harmony='other'
        )

        self.violet_red36 = ColorScheme(
            name='violet_red36',
            colors=['#D85332','#DB9328','#FFE4B0','#63A597','#513143'],
            harmony='other'
        )

        self.violet_red37 = ColorScheme(
            name='violet_red37',
            colors=['#A54979','#E69FBB','#689096','#F3CC4E','#64686A'],
            harmony='other'
        )

        self.violet_red38 = ColorScheme(
            name='violet_red38',
            colors=['#C30455','#9C3F7C','#7479A2','#A5AB92','#D5DD81'],
            harmony='other'
        )

        self.violet_red39 = ColorScheme(
            name='violet_red39',
            colors=['#FF5EE6','#FF3C9C','#FF6066','#F18B00','#FFF19A'],
            harmony='other'
        )

        # page 180
        self.violet_red40 = ColorScheme(
            name='violet_red40',
            colors=['#918282','#FFC694','#F9FEFA','#691C21','#6A406E'],
            harmony='other'
        )

        self.violet_red41 = ColorScheme(
            name='violet_red41',
            colors=['#434241','#56785D','#DB8F38','#CF6549','#992E4D'],
            harmony='other'
        )

        self.violet_red42 = ColorScheme(
            name='violet_red42',
            colors=['#2B2032','#8D3A5E','#EF5489','#F17F54','#F2A81F'],
            harmony='other'
        )

        self.violet_red43 = ColorScheme(
            name='violet_red43',
            colors=['#D4174D','#FCB10F','#88A807','#2884A4','#600A72'],
            harmony='other'
        )

        self.violet_red44 = ColorScheme(
            name='violet_red44',
            colors=['#67B89D','#6C4B66','#700D48','#9C4646','#D18B45'],
            harmony='other'
        )

        self.violet_red45 = ColorScheme(
            name='violet_red45',
            colors=['#F6EEC9','#F67489','#DB3B64','#6D3650','#283646'],
            harmony='other'
        )

        self.violet_red46 = ColorScheme(
            name='violet_red46',
            colors=['#233346','#CD7C49','#D22921','#66152A','#2B0B1A'],
            harmony='other'
        )

        self.violet_red47 = ColorScheme(
            name='violet_red47',
            colors=['#9AC6D1','#A3ABA2','#A8A345','#B34F6B','#B22456'],
            harmony='other'
        )






    def display_examples(self):
        schemes = np.random.choice(len(list(vars(self).values())), 16)
        schemes = np.array(list(vars(self).values()))[schemes]
        fig, axes = plt.subplots(4,4,figsize=(6,6),dpi=100)
        i = 0
        for ax in axes.flatten():
            scheme = schemes[i]
            for j in range(len(scheme.colors)):
                ax.plot(np.linspace(0,1,10),np.zeros(len(np.linspace(0,1,10)))-j,c=scheme.colors[j],linewidth=19)
            ax.set_title(scheme.name)
            ax.axis('off')
            ax.set_ylim(1,-4.35)
            i += 1
        fig.tight_layout()

    def display_scheme(self, name):
        # where name is a string of the color scheme name
        # for instance, yellow_green26
        names = np.array([list(vars(self).values())[i].name for i in range(len(list(vars(self).values())))])
        if name not in names:
            print(name+' is not a valid color scheme name.')
        else:
            index = int(np.where(names == name)[0][0])
            scheme = list(vars(self).values())[index]
            plt.figure()
            for i in range(len(scheme.colors)):
                plt.plot(np.linspace(0,1,10),np.linspace(0,1,10)-i,c=scheme.colors[i],linewidth=50)
                plt.text(x=.45, y=-i+0.4, s=scheme.colors[i],rotation=10)
            plt.axis('off')
            plt.title(scheme.name)
            plt.show()

    def hex_to_rgb(self, hex_string):
        # inputs a hex string such as #CD7C46
        return [int(hex_string[i:i+2], 16) for i in (1, 3, 5)]

    def rgb_to_hex(self, rgb):
        # inputs an rgb list such as [205, 124, 70]
        return f"#{int(rgb[0]):02x}{int(rgb[1]):02x}{int(rgb[2]):02x}"

    def colorblindness_test(self, hex_string):
        # input is a hex string such as #CD7C46
        # returns a 5-element list of hex strings transformed by colorblindness matrices 
        # for protanopia, euteranopia, tritanopia, protanomaly, and deuteranomaly
        rgb_array = np.array(self.hex_to_rgb(hex_string)) / 255.0

        # colorblindness arrays from https://gist.github.com/Lokno/df7c3bfdc9ad32558bb7?permalink_comment_id=3943065
        Protanopia   = np.array([[0.567,0.433,0.000],
                               [0.558,0.442,0.000],
                               [0.000,0.242,0.758]])

        Deuteranopia = np.array([[0.625,0.375,0.000],
                               [0.700,0.300,0.000],
                               [0.000,0.300,0.700]])

        Tritanopia   = np.array([[0.950,0.050,0.000],
                                [0.000,0.433,0.567],
                                [0.000,0.475,0.525]])

        Protanomaly  = np.array([[0.817,0.183,0.000],
                                 [0.333,0.667,0.000],
                                 [0.000,0.125,0.875]])

        Deuteranomaly= np.array([[0.800,0.200,0.000],
                                [0.258,0.742,0.000],
                                [0.000,0.142,0.858]])

        colorblind_matrices = [Protanopia, Deuteranopia, Tritanopia, Protanomaly, Deuteranomaly]

        hex_transformed = []
        for i in range(len(colorblind_matrices)):
            rgb_transformed = colorblind_matrices[i] @ rgb_array 
            rgb_transformed = np.clip(rgb_transformed * 255, 0, 255)
            hex_transformed.append(self.rgb_to_hex(rgb_transformed))

        return hex_transformed

    def scheme_colorblindness(self, name):
        # where name is the name of the scheme, 
        # e.g. yellow_green26
        names = np.array([list(vars(self).values())[i].name for i in range(len(list(vars(self).values())))])
        if name not in names:
            print(name+' is not a valid color scheme name.')
        else:
            index = int(np.where(names == name)[0][0])
            scheme = list(vars(self).values())[index]
            scheme_colors = np.array(scheme.colors).reshape(1,-1)
        
            # precompute the colorblind transformed versions of that scheme
            colorblind_simulated = np.array([self.colorblindness_test(scheme.colors[i]) for i in range(len(scheme.colors))]).T
            schemes = np.concatenate((scheme_colors, colorblind_simulated))
            titles = ['true','protanopia', 'deuteranopia', 'tritanopia', 'protanomaly', 'deuteranomaly']
            fig, axes = plt.subplots(2,3)
            for i, ax in enumerate(axes.flatten()):
                for j in range(0,len(scheme.colors)):
                    ax.plot(np.linspace(0,1,10),np.zeros(len(np.linspace(0,1,10)))-j,c=schemes[i][j],linewidth=30)
                ax.set_title(titles[i])
                ax.axis('off')
                ax.set_ylim(1,-4.35)
            fig.tight_layout()
            plt.suptitle(scheme.name,y=1.03,fontweight='bold',fontsize=15)
            plt.show()

    def custom_colorblindness(self, custom_scheme):
        # input is a list of hex values
        scheme_colors = np.array(custom_scheme).reshape(1,-1)
        # precompute the colorblind transformed versions of that scheme
        colorblind_simulated = np.array([self.colorblindness_test(custom_scheme[i]) for i in range(len(custom_scheme))]).T
        schemes = np.concatenate((scheme_colors, colorblind_simulated))
        titles = ['true','protanopia', 'deuteranopia', 'tritanopia', 'protanomaly', 'deuteranomaly']
        
        fill_intervals = np.linspace(0,1,len(custom_scheme)+1)
        fig, axes = plt.subplots(2,3)
        for i, ax in enumerate(axes.flatten()):
            for j in range(0,len(custom_scheme)):
                ax.fill_between([0,1],
                                [fill_intervals[j], fill_intervals[j]],
                                [fill_intervals[j+1],fill_intervals[j+1]],
                                color=schemes[i][j])
            ax.set_title(titles[i])
            ax.set_ylim(0,1)
            ax.set_ylim(0,1)
            ax.axis('off')
        fig.tight_layout()
        plt.show()

    def scheme_to_cmap(self, name):
        # where name is the name of the scheme, 
        # e.g. yellow_green26
        names = np.array([list(vars(self).values())[i].name for i in range(len(list(vars(self).values())))])
        if name not in names:
            print(name+' is not a valid color scheme name.')
        else:
            index = int(np.where(names == name)[0][0])
            scheme = list(vars(self).values())[index]
            mpl_cmap = LinearSegmentedColormap.from_list(scheme.name, scheme.colors)

            return mpl_cmap

    def custom_scheme_to_cmap(self, custom_scheme):
        # input is a list of hex values
        mpl_cmap = LinearSegmentedColormap.from_list('custom_scheme', custom_scheme)
        return mpl_cmap
        
        
ColorSchemes = color_schemes()