import random
class Bridge:
    def __init__(self, length):
        self.i = 0
        self.length = length
        self.brlist = []
        for i in range(length):
            num = random.randrange(0, 2)
            self.brlist.append(num)
    def build(self, 입력방향, i):
        if 입력방향 == "U":
            self.buildUp(i)
            if self.brlist[i] == 1:
                print("O", end=" ")
            else:
                print("X", end=" ")
            print("]")
            self.buildDown(i)
            print(" ", end=" ")
            print("]")
            if self.brlist[i] != 1:
                return [False, True, self.i+1]
        if 입력방향 == "D":
            self.buildUp(i)
            print(" ", end=" ")
            print("]")
            self.buildDown(i)
            if self.brlist[i] == 0:
                print("O", end=" ")
            else:
                print("X", end=" ")
            print("]")
            if self.brlist[i] != 0:
                return [False, True, self.i+1]
        return [True, True, self.i+1]
    def buildUp(self, i):
        print("[", end=" ")
        for j in range(i):
            if self.brlist[j] == 1:
                print("O", end=" ")
            else:
                print(" ", end=" ")
            if j != i:
                print("|", end=" ")
    def buildDown(self, i):
        print("[", end=" ")
        for j in range(i):
            if self.brlist[j] == 1:
                print(" ", end=" ")
            else:
                print("O", end=" ")
            if j != i:
                print("|", end=" ")
    def success(self, lasttemp, attempts):
        print("최종 게임 결과")
        self.buildUp(self.i-1)
        if lasttemp == 1:
            print("O", end=" ")
        else:
            print(" ", end=" ")
        print("]")
        self.buildDown(self.i - 1)
        if lasttemp == 1:
            print(" ", end=" ")
        else:
            print("O", end=" ")
        print("]")
        print("게임 성공 여부 : 성공")
        print("총 시도한 횟수 : {0}".format(attempts))
    def retry(self, attempts, lasttemp):
        retrycontrol = input("게임을 다시 시도할지 여부를 입력해주세요. (재시도: R, 종료: Q)\n")
        if retrycontrol == "R":
            attempts = attempts + 1
            return [retrycontrol, True, attempts, 0]
        else:
            return self.fail(retrycontrol, lasttemp, attempts)
    def fail(self, retrycontrol, lasttemp, attempts):
        print("최종 게임 결과")
        self.buildUp(self.i-1)
        if lasttemp == 1:
            print("X ]")
        else:
            print("  ]")
        self.buildDown(self.i-1)
        if lasttemp == 0:
            print("X ]")
        else:
            print("  ]")
        print("게임 성공 여부 : 실패")
        print("총 시도한 횟수 : {0}".format(attempts))
        return [retrycontrol, False]

#다리 건너기 게임 시작
print("다리 건너기 게임을 시작합니다.\n")
length = int(input("다리의 길이를 입력해주세요.\n"))
bridge = Bridge(length)
bridge_status = True
retry_status = True
game_success = False
attempts = 1

while retry_status == True:
    while bridge.i < length and bridge_status == True:
        # 이동할 칸 선택
        입력방향 = input("이동할 칸을 선택해주세요. (위 : U, 아래 : D)\n")
        if 입력방향 == "U":
            lasttemp = 1
        else:
            lasttemp = 0
        print(bridge.brlist)
        [bridge_status, retry_status, bridge.i] = bridge.build(입력방향, bridge.i)
    if bridge.i == length and bridge_status == True:
        game_success = True
        retry_status = False
    else:
        result = bridge.retry(attempts, lasttemp)
        if result[0] == "R":
            bridge_status = result[1]
            attempts = result[2]
            bridge.i = result[3]
        else:
            retry_status = result[1]
if game_success == True:
    bridge.success(lasttemp, attempts)