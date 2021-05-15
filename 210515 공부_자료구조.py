# 단일 연결 리스트
class SLinkedList:
    # S_L_list에서 쓸 노드
    class Node:
        def __init__(self, v, n=None):  # Node클래스(새데이터, next로보낼값)
            self.value = v  # 새로 저장된 데이터
            self.next = n   # next: 다음 노드를 가리키는 변수
    # S_L_List에서 필요한 변수
    def __init__(self):
        self.head = None    # 첫 생성시 내부에 노드 시작 지점 표시
    # 삽입
    # head 쪽에 노드를 계속 추가하는 방식
    def insertNode(self, v):    # 추가할 데이터 v
        if self.head is None:   # 저장된 노드 없는 경우
            self.head = self.Node(v)    # 새로운 노드를 head에 저장
        else:   # 저장된 노드가 있는 경우
            self.head = self.Node(v, self.head) # 새노드를 head, 기존노드는 next로 보냄
    # 출력
    def printNode(self):
        # 저장된 노드가 없을 때
        if self.head is None:   ## ==: 값의 일치, is: 객체의 일치
            print("저장된 데이터가 없음")
            return  ## if문 return 처리 잊지 말자
        else:
            print("현재 리스트 구조:", end='\t')
            link = self.head
            while link :    # link는 저장노드가 있을 때만 생성됨. next가 None일 때까지와 동일한 조건. ##??
                print(link.value, '->', end=' ')
                link = link.next
            print()
    # 삭제
    ## C언어와 달리 JAVA, Python은 삭제된 데이터의 메모리해제는 신경쓰지 않음
    ## 이 경우 관리에서 벗어난 데이터는 가비지컬렉션으로 알아서 처리함
    ## 삭제된 데이터를 관리체계에서 제외하도록 함
    def deleteNode(self):
        if self.head is None:
            print("삭제할 노드가 없음")
            return
        else:
            self.head = self.head.next  # head를 next로 넘긴다
    # 탐색
    ## 찾고자 하는 데이터를 가진 노드가 발견되면 중지!
    ## 해당 노드가 몇 번 째 노드인지 반환하기
    ## 못찾으면 탐색 실패의 의미인 None을 반환하기
    def searchNode(self, v):
        if self.head is None:
            print("저장된 데이터 없음")
            return
        else:
            link = self.head
            index = 0
            while link:
                if v == link.value:
                    print("{}의 위치: {}".format(v, index))
                    return index    # if문에서 꼭 return 하자
                else:
                    link = link.next
                    index += 1
            print("해당값을 가진 노드가 없습니다")



#---------테스트----------


if __name__=="__main__":
    sl = SLinkedList()
    sl.printNode()  # 출력
    sl.insertNode('1st')
    sl.insertNode('2nd')
    sl.insertNode('3rd')
    sl.printNode()  #출력
    print("노드 위치 탐색:")
    sl.searchNode('1st')
