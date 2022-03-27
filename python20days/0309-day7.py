import time

 

input("엔터를 누르고 5초를 셉니다.")

start = time.time()

 

input("5초 후에 다시 엔터를 누릅니다.")

end = time.time()

 

et = end - start   # end 시간에서 start 시간을 빼면 실제 걸린 시간을 계산할 수 있습니다.

print("실제 시간 :", et, "초")

print("차이 :", abs(et - 5), "초")
