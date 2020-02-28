import numpy as np
 
from gnuradio import gr
from time import sleep 
from math import sqrt,atan , pi,floor

class blk(gr.sync_block):
  def __init__(self, viewDebug = 0 ):
  
        gr.sync_block.__init__(self,
                            name ='Le Machin de Python' , 
                            in_sig= [np.int8],
                            out_sig= None
        ) 
        self.viewDebug = viewDebug
        self.trame = np.array([] , np.int8)
        self.table ="#ABCDEFGHIJKLMNOPQRSTUVWXYZ#####_###############0123456789#####"
   
  def decodetrame112(self,S):
      df= int(S[0:5], 2)
      if df== 17 :
         ca = int(S[5:8] , 2)
         ica024 = int(S[8:32], 2)
         tc = int(S[32:37], 2)
         tct=0
         if tc in range(9 ,19):
            km= "" 
            alt= S[40:52]
            q= alt[7] 
            n = alt[:7]+ alt[8:]
            if q == "1":
                 n=int (n,2) * 25
            else:
                 n= int(n,2) * 100
            km = ( n -1000) * 0.3048
#------------------------------------------Modifications------------------------------------------------           
            i = int(S[53],2)
            lat= int(S[54:71],2)
            lon = int(S[71:88],2)
            lat_cpr_even = lat /131072
            lon_cpr_even = lon/131072
            lat_cpr_odd =  lat / 131072
            lon_cpr_odd = lon/131072
            dlat_even = 90 /60
            dlat_odd = 90/59
            j = floor (59 * lat_cpr_even - 60 * lat_cpr_odd + 0.5)
            latitude = float(dlat_even * (j%60 + lat_cpr_even))
            print tc, " ",hex(ica024), "latitude  = ",latitude," deg Nord"
#----------------------------------------Modification---------------------------------------------------            
            print tc, " " ,hex(ica024) , " ", km , "m"
            tct=1
         if  tc in range(1,5):
            ec= int(S[37:40], 2)
            ident = ""   
            for i in range(0, 8):
                  c= int(S[40 + i * 6:46 + i * 6], 2 ) 
                  ident= ident + self.table[c]
            print tc, " " , hex(ica024) , " " , ident 
            tct= 1

         if tc == 19:
            st = int(S[37:40])
            swe = S[45]
            vwe = int(S[46:56], 2)
            sns = S[56]
            vns = int(S[57:67], 2)
            vwe = float(vwe)
            vns = float(vns)
            if vns ==0 : vns = 0.0001
            vitesse = sqrt(vwe * vwe + vns * vns)  / 0.539957
            heading = atan(vwe / vns) * (360.0 / (2.0 * pi))
            if swe == "0" and sns == "1" :
                    heading = 180.0 - heading
            if swe == "1" and sns == "1" :
                    heading = 180.0 +heading
            if swe == "1" and sns == "0" :         
                    heading == 360.0 - heading   
            print tc, " ", hex(ica024), "vitesse = ", int(vitesse), " km/h", " cap = ", int(heading), "deg"
            tct = 1

      
         if tct == 0:
                print tc, "tc non traite"
      else:
         if self.viewDebug:
                     print df,"***********************trame112******************************"

  def decodetrame56(self, S):
            df = int(S[0:5], 2)
            
            if self.viewDebug:
                    print df, "************trame52************"
            return

  def decodetrame(self):

        S = ""
        for i in range(0, 224):
            if self.trame[0] == self.trame[1]:
                    break
            if self.trame[0] == 1:
                    S = S + "1"
            else:
                    S = S + "0"
            self.trame = self.trame[2:]
#-------------------------------------------------Modification --CRC--------------
        if self.check(S):

          if len(S) == 112:

             self.decodetrame112(S)

          if len(S) == 56:
      
            self.decodetrame56(S)

        else:
        	if self.viewDebug:
        		print "trame alteree: " , S
#--------------------------------------------------Calcul CRC--------------------------------        		
  def check(self,t):
      generator = "1111111111111010000001001"   
      t = list(t)  
      for i in range(0,len(t)-24):
      	if t[i] == "1" : 
           for j in range(len(generator)):
      	    	t[i+j] =str( (int(t[i+j]) ^ int(generator[j])) )
      t=''.join(t[-24:]) 
      if t == "0"*24 :
      	 if self.viewDebug:
      	  print t , "-*-*--*-*-*-*-*-*-*-*-*-*-*"
         return True
      return False 
#-------------------------------------------Calcule CRC ----------------------------------------             


  def work(self, input_items, output_items):
        """ads-b decoder"""
        self.trame = np.append(self.trame, input_items[0])
        
        bits1 = np.where(self.trame ==1)[0]
        if len(bits1) == 0:
                self.trame = self.trame[-1:]
        while len(bits1) > 0:
                self.trame = self.trame[bits1[0]:]
                bits1 = bits1[1:]
                if len(self.trame) >241:
                    sr = 0
                    for i in range(0, 14):
                       sr = (sr << 1) | self.trame[i]

                    if sr == 0b10000101000000:
                        self.trame = self.trame[14:]
                        self.decodetrame()
                        bits1 = np.where(self.trame == 1)[0]
                    
                    if len(bits1) == 0: self.trame = self.trame[-1:]; break;
                else:
                    break
        return len(input_items[0])




