import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtCore import QDateTime
#관리자 장바구니
count1 = 0
totalprice1 = 0
menusss = {}
# 카드 결제 초
cnt = 5
# 대기 화면 초
cntt = 20
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("pmj.ui")[0]
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QWidget, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(5)
        self.stackedWidget_5.setCurrentIndex(0)
        #대기화면이동
        self.bb.clicked.connect(self.first)
        self.cc.clicked.connect(self.first)
        # 메인화면 가기
        self.btn3.clicked.connect(self.first)
        self.btn5.clicked.connect(self.first)
        self.btn6.clicked.connect(self.first)
        #주문 화면
        self.btn1.clicked.connect(self.menu)
        self.btn2.clicked.connect(self.menu)
        #관리자화면
        self.btn0.clicked.connect(self.user)
        #메뉴선택 이동
        self.btn11.clicked.connect(self.menu111)
        self.btn15.clicked.connect(self.menu111)
        self.btn19.clicked.connect(self.menu111)
        self.btn23.clicked.connect(self.menu111)
        self.btn12.clicked.connect(self.menu222)
        self.btn16.clicked.connect(self.menu222)
        self.btn20.clicked.connect(self.menu222)
        self.btn24.clicked.connect(self.menu222)
        self.btn13.clicked.connect(self.menu333)
        self.btn17.clicked.connect(self.menu333)
        self.btn21.clicked.connect(self.menu333)
        self.btn25.clicked.connect(self.menu333)
        self.btn14.clicked.connect(self.menu444)
        self.btn18.clicked.connect(self.menu444)
        self.btn22.clicked.connect(self.menu444)
        self.btn26.clicked.connect(self.menu444)
        #결제화면
        self.btn41.clicked.connect(self.menu2)
        self.btn42.clicked.connect(self.menu22)
        self.btn61.clicked.connect(self.menu3)
        self.btn62.clicked.connect(self.menu4)

        #장바구니 추가
        self.bt1.clicked.connect(lambda:self.add("참치김밥",0,0,0,0))
        self.bt2.clicked.connect(lambda:self.add("소고기김밥",0,0,0,0))
        self.bt3.clicked.connect(lambda:self.add("치즈김밥",0,0,0,0))
        self.bt4.clicked.connect(lambda:self.add("제육김밥",0,0,0,0))
        self.bt5.clicked.connect(lambda:self.add("멸치김밥",0,0,0,0))
        self.bt6.clicked.connect(self.ch) #추가선택사항
        self.bt7.clicked.connect(self.ch2) #추가선택사항
        self.bt8.clicked.connect(self.ch3) #추가선택사항
        self.bt9.clicked.connect(self.ch4) #추가선택사항
        self.bt6.clicked.connect(lambda: self.tpadd("떡볶이",0,0,0,0))
        self.bt7.clicked.connect(lambda: self.tpadd("떡순튀",0,0,0,0))
        self.bt8.clicked.connect(lambda: self.tpadd("짜장떡볶이",0,0,0,0))
        self.bt9.clicked.connect(lambda: self.tpadd("마라떡볶이",0,0,0,0))
        self.bt10.clicked.connect(lambda: self.add("순대",0,0,0,0))
        self.bt11.clicked.connect(lambda: self.add("군만두",0,0,0,0))
        self.bt12.clicked.connect(lambda: self.add("오징어튀김",0,0,0,0))
        self.bt13.clicked.connect(lambda: self.add("김말이",0,0,0,0))
        self.bt14.clicked.connect(lambda: self.add("우동",0,0,0,0))
        self.bt15.clicked.connect(lambda: self.add("돈가스",0,0,0,0))
        self.bt16.clicked.connect(lambda: self.add("물냉면",0,0,0,0))
        self.bt17.clicked.connect(lambda: self.add("제육덮밥",0,0,0,0))
        self.bt18.clicked.connect(lambda: self.add("콩나물국밥",0,0,0,0))
        self.bt19.clicked.connect(lambda: self.add("김치볶음밥",0,0,0,0))
        self.bt20.clicked.connect(lambda: self.add("치킨",0,0,0,0))
        self.bt21.clicked.connect(lambda: self.add("양념치킨",0,0,0,0))
        self.bt22.clicked.connect(lambda: self.add("콜라",0,0,0,0))
        self.bt23.clicked.connect(lambda: self.add("사이다",0,0,0,0))
        self.bt24.clicked.connect(lambda: self.add("소주",0,0,0,0))
        self.bt25.clicked.connect(lambda: self.add("맥주",0,0,0,0))


        #장바구니 삭제
        self.btnremove.clicked.connect(self.remove)
        #현금 입금
        self.btnmoney1.clicked.connect(self.money1)
        #현금영수증
        self.btn71.clicked.connect(self.money2)
        self.btn72.clicked.connect(self.end)
        #현금영수증 번호
        self.btn73.clicked.connect(self.moneynumber)
        #카드 삽입
        self.inputcard.clicked.connect(self.menu5)

        # 결제화면 이동
        self.btn4.clicked.connect(self.paypage)
        # 관리자 로그인
        self.btnpw.clicked.connect(self.login)
        self.tp = [0,0,0,0,0]
        self.mmenu = {}
        #장바구니
        self.menuss = {}
        #가격
        self.menus = {
            '참치김밥': 4000,
            '소고기김밥':4000,
            '치즈김밥' : 4000,
            '제육김밥' : 4000,
            '멸치김밥' : 3000,
            "떡볶이" : 5000,
            "떡순튀": 7000,
            "짜장떡볶이": 6000,
            "마라떡볶이": 6000,
            "순대": 3000,
            "군만두": 5000,
            "오징어튀김": 1000,
            "김말이": 1000,
            "우동": 5000,
            "돈가스": 8000,
            "물냉면": 7000,
            "제육덮밥": 8000,
            "콩나물국밥": 5000,
            "김치볶음밥": 8000,
            "치킨": 15000,
            "양념치킨": 15000,
            "콜라": 2000,
            "사이다": 2000,
            "소주": 5000,
            "맥주": 5000,
            "치즈추가":1500,
            "떡추가":1000,
            "어묵추가":1000,
            "계란추가":500}
        #장바구니
        self.totalprice = 0
        self.count = 0
        #관리자 장바구니
        global count
        global totalprice
        # 카드경고문 빨간색 변경
        self.lb123.setStyleSheet("color:red;")
        #시계 설정
        self.timerr = QTimer(self)
        self.timerr.timeout.connect(self.time1)
        self.timerr.start(1000)
        # 첫 로그인
        self.btnflogin.clicked.connect(self.floginh)
        # 대기화면 벗어남
        self.aa.clicked.connect(self.llogin)
        #관리자 비밀번호 초기화
        self.userpwpw.clicked.connect(self.idclear)

        self.tp1.clicked.connect(lambda:self.tpadd("떡볶이",1,0,0,0))
        self.tp2.clicked.connect(lambda:self.tpadd("떡볶이",0,1,0,0))
        self.tp3.clicked.connect(lambda:self.tpadd("떡볶이",0,0,1,0))
        self.tp4.clicked.connect(lambda:self.tpadd("떡볶이",0,0,0,1))
        self.tp5.clicked.connect(lambda: self.tpadd("떡순튀", 1, 0, 0, 0))
        self.tp6.clicked.connect(lambda: self.tpadd("떡순튀", 0, 1, 0, 0))
        self.tp7.clicked.connect(lambda: self.tpadd("떡순튀", 0, 0, 1, 0))
        self.tp8.clicked.connect(lambda: self.tpadd("떡순튀", 0, 0, 0, 1))
        self.tp9.clicked.connect(lambda: self.tpadd("짜장떡볶이", 1, 0, 0, 0))
        self.tp10.clicked.connect(lambda: self.tpadd("짜장떡볶이", 0, 1, 0, 0))
        self.tp11.clicked.connect(lambda: self.tpadd("짜장떡볶이", 0, 0, 1, 0))
        self.tp12.clicked.connect(lambda: self.tpadd("짜장떡볶이", 0, 0, 0, 1))
        self.tp13.clicked.connect(lambda: self.tpadd("마라떡볶이", 1, 0, 0, 0))
        self.tp14.clicked.connect(lambda: self.tpadd("마라떡볶이", 0, 1, 0, 0))
        self.tp15.clicked.connect(lambda: self.tpadd("마라떡볶이", 0, 0, 1, 0))
        self.tp16.clicked.connect(lambda: self.tpadd("마라떡볶이", 0, 0, 0, 1))
        self.tpyes.clicked.connect(self.tpadd2)
        self.tpyes2.clicked.connect(self.tpadd2)
        self.tpyes3.clicked.connect(self.tpadd2)
        self.tpyes4.clicked.connect(self.tpadd2)
    def tpadd(self,product,tpa,tpb,tpc,tpd):
        price = self.menus[product]
        if tpa > 0:
            self.tp[0] += 1
        if tpb > 0:
            self.tp[1] += 1
        if tpc > 0:
            self.tp[2] += 1
        if tpd > 0:
            self.tp[3] += 1
        self.tp[4] = product
    def tpadd2(self):
        tpa = self.tp[0]
        tpb = self.tp[1]
        tpc = self.tp[2]
        tpd = self.tp[3]
        product = self.tp[4]
        price = self.menus[product]
        key = (product,price,tpa,tpb,tpc,tpd)
        self.totalprice += (price+(1000*tpa) + (1500*tpb) + (1000*tpc) + (500*tpd))
        self.count += 1
        global count1
        global totalprice1
        global menusss
        count1 += 1
        totalprice1 += (price+(1000*tpa) + (1500*tpb) + (1000*tpc) + (500*tpd))
        self.total.clear()
        self.usermenu2.clear()
        self.total.addItem(f"총{self.count}개 {self.totalprice}원 입니다.")
        self.usermenu2.addItem(f"총 매출 {count1}개 {totalprice1}원 입니다.")
        self.listwidgetcheck.clear()
        self.listwidgetcheck.addItem(f"총{self.count}개 {self.totalprice}원 입니다.")
        if tpa == 0 and tpb == 0 and tpc == 0 and tpd == 0:
            key = (product, price, tpa, tpb, tpc, tpd)
            if key in self.menuss:
                self.menuss[key] += 1
            else:
                self.menuss[key] = 1
        else:
            if key in self.menuss:
                self.menuss[key] += 1
            else:
                self.menuss[key] = 1
        if tpa == 0 and tpb == 0 and tpc == 0 and tpd == 0:
            key = (product, price, tpa, tpb, tpc, tpd)
            if key in menusss:
                menusss[key] += 1
            else:
                menusss[key] = 1
        else:
            if key in menusss:
                menusss[key] += 1
            else:
                menusss[key] = 1
        self.update_order_list()
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)
        self.tp = [0, 0, 0, 0, 0]
        tpa = 0
        tpb = 0
        tpc = 0
        tpd = 0


    # 장바구니 추가
    def add(self,product,tpa,tpb,tpc,tpd):
        price = self.menus[product]
        self.totalprice += price
        self.count += 1
        global count1
        global totalprice1
        global menusss
        count1 += 1
        totalprice1 += price
        self.total.clear()
        self.usermenu2.clear()
        self.total.addItem(f"총{self.count}개 {self.totalprice}원 입니다.")
        self.usermenu2.addItem(f"총 매출 {count1}개 {totalprice1}원 입니다.")
        self.listwidgetcheck.clear()
        self.listwidgetcheck.addItem(f"총{self.count}개 {self.totalprice}원 입니다.")
        key = (product,price,tpa,tpb,tpc,tpd)
        if key in self.menuss:
            self.menuss[key] += 1
        else:
            self.menuss[key] = 1
        if key in menusss:
            menusss[key] += 1
        else:
            menusss[key] = 1
        self.update_order_list()
    # 장바구니 제거
    def remove(self):
        selectitem = self.order.currentItem()
        if selectitem:
            produ = selectitem.text()
            a = produ.split(" ")
            b = a[0]
            mprice = self.menus[b]
            global menusss
            global count1
            global totalprice1
            if '+' in a[3]:
                c = int(a[6])
                d = int(a[9])
                e = int(a[12])
                f = int(a[15])
                key = (b,mprice,c,d,e,f)
                if key in self.menuss and self.menuss[(b, mprice,c,d,e,f)] > 1:
                    self.menuss[key] -= 1
                else:
                    del self.menuss[key]
                if key in menusss and menusss[(b, mprice, c, d, e, f)] > 1:
                    menusss[key] -= 1
                else:
                    del menusss[key]
                totalprice1 -= (mprice + (1000 * c) + (1500 * d) + (1000 * e) + (500 * f))
                self.totalprice -= (mprice + (1000 * c) + (1500 * d) + (1000 * e) + (500 * f))
            else:
                key = (b, mprice,0,0,0,0)
                if key in self.menuss and self.menuss[(b, mprice,0,0,0,0)] > 1:
                    self.menuss[key] -= 1
                else:
                    del self.menuss[key]
                if key in menusss and menusss[(b, mprice,0,0,0,0)] > 1:
                    menusss[key] -= 1
                else:
                    del menusss[key]
                self.totalprice -= mprice
                totalprice1 -= mprice
            self.count -= 1
            count1 -= 1
            self.usermenu2.clear()
            self.total.clear()
            self.total.addItem(f"총{self.count}개 {self.totalprice}원 입니다.")
            self.usermenu2.addItem(f"총{count1}개 {totalprice1}원 입니다.")
            self.update_order_list()
        else:
            QMessageBox.warning(self, "주의", "제거할 항목을 선택해주세요")

    # 장바구니 표시
    def update_order_list(self):
        self.order.clear()
        self.order2.clear()
        self.usermenu1.clear()
        for (product, price,tpa,tpb,tpc,tpd),a in self.menuss.items():
            if tpa == 0 and tpb == 0 and tpc == 0 and tpd == 0:
                self.order.addItem(f"{product} {a}개  {price * a}원")
                self.order2.addItem(f"{product} {a}개  {price * a}원")
            else:
                tpprice = (1000*tpa) + (1500*tpb) + (1000*tpc) + (500*tpd)
                self.order.addItem(f"{product} {a}개  {price * a}+{tpprice}원 토핑 떡 {tpa} 번 치즈 {tpb} 번 어묵 {tpc} 번 계란 {tpd} 번")
                self.order2.addItem(f"{product} {a}개  {price * a}원 토핑 떡 {tpa} 번 치즈 {tpb} 번 어묵 {tpc} 번 계란 {tpd} 번")
        for (product, price,tpa,tpb,tpc,tpd),a in menusss.items():
            if tpa == 0 and tpb == 0 and tpc == 0 and tpd == 0:
                self.usermenu1.addItem(f"{product} {a}개  {price * a}원")
            else:
                tpprice = (1000*tpa) + (1500*tpb) + (1000*tpc) + (500*tpd)
                self.usermenu1.addItem(f"{product} {a}개  {price * a}+{tpprice}원 토핑 떡 {tpa} 번 치즈 {tpb} 번 어묵 {tpc} 번 계란 {tpd} 번")

    #관리자 비밀번호 초기화 후 초기화면 이동
    def idclear(self):
        with open('id','w') as file:
            file.write("")
        self.stackedWidget.setCurrentIndex(6)
        self.userpw.clear()
        self.flogin.clear()
    # 회원가입 혹은 메인화면 이동
    def llogin(self):
        with open("id",'r') as file:
            id = file.read()
        if id.isdigit() and len(id) == 6:
            self.first()
        else:
            self.stackedWidget.setCurrentIndex(6)
    #관리자 회원가입
    def floginh(self):
        pw = self.flogin.text()
        if pw.isdigit() and len(pw) == 6:
            with open('id','w') as file:
                file.write(pw)
            self.first()
            self.flogin.clear()
        else:
            QMessageBox.warning(self,"경고","숫자 6자리를 입력해주세요")
            self.flogin.clear()
    # 대기화면 설정
    def first(self):
        self.stackedWidget.setCurrentIndex(0)
        self.tp = [0,0,0,0,0]
        global  cntt
        cntt = 20
        self.timet.setText(str(20))
        self.timettt()
    def timettt(self):
        self.timerrr = QTimer(self)
        self.timerrr.timeout.connect(self.time2)
        self.timerrr.start(1000)
    #잠수화면
    def time2(self):
        global cntt
        cntt -= 1
        self.timet.setText(str(cntt))
        if cntt == -1:
            a = random.randint(0,2) #대기화면 랜덤
            self.stackedWidget.setCurrentIndex(5)
            self.stackedWidget_5.setCurrentIndex(a)
            self.timerrr.stop()
    #시계설정
    def time1(self):
        currenttime = QDateTime.currentDateTime()
        self.time.setDateTime(currenttime)
    #추가선택사항 화면 이동
    def ch(self):
        self.stackedWidget_2.setCurrentIndex(5)
    def ch2(self):
        self.stackedWidget_2.setCurrentIndex(6)
    def ch3(self):
        self.stackedWidget_2.setCurrentIndex(7)
    def ch4(self):
        self.stackedWidget_2.setCurrentIndex(8)
    #추가선택사항 복귀
    def btpcp(self):
        self.stackedWidget_2.setCurrentIndex(1)
    #현금영수증 입력화면 이동
    def money2(self):
        self.stackedWidget_3.setCurrentIndex(4)
    #현금 영수증 아니요 마무리 화면으로 바로 이동
    def end(self):
        self.stackedWidget.setCurrentIndex(4)
        self.total.clear()
        self.order.clear()
        self.order2.clear()
        self.count = 0
        self.totalprice = 0
        self.menuss = {}
    #현금영수증 확인
    def moneynumber(self):
        a = self.money13.toPlainText()
        if a.isdigit() and (len(a)== 10 or len(a)== 11 or len(a) == 12):
            QMessageBox.information(self,"성공","현금영수증 처리가 완료되었습니다.")
            self.stackedWidget.setCurrentIndex(4)
            self.total.clear()
            self.order.clear()
            self.order2.clear()
            self.count = 0
            self.totalprice = 0
            self.menuss = {}
        else:
            QMessageBox.warning(self,"실패","번호를 다시 입력해주세요 올바르지 않습니다.")
            self.money13.clear()
    #결제화면 이동
    def paypage(self):
        a = len(self.menuss)
        if a > 0:
            self.stackedWidget.setCurrentIndex(2)
            self.stackedWidget_3.setCurrentIndex(0)
        else:
            QMessageBox.warning(self,"경고","장바구니가 비었습니다.")
    #메뉴선택 이동
    def menu444(self):
        self.stackedWidget_2.setCurrentIndex(3)
    def menu333(self):
        self.stackedWidget_2.setCurrentIndex(2)

    def menu222(self):
        self.stackedWidget_2.setCurrentIndex(1)

    def menu111(self):
        self.stackedWidget_2.setCurrentIndex(0)
    #주문화면 이동
    def menu(self):
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        self.timerrr.stop()
    #관리자화면 이동
    def user(self):
        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_4.setCurrentIndex(0)
        self.timerrr.stop()
        self.userpw.clear()    #결제화면 이동
    def menu22(self):
        self.stackedWidget.setCurrentIndex(1)
    def menu2(self):
        self.stackedWidget_3.setCurrentIndex(1)
    def menu3(self):
        self.stackedWidget_3.setCurrentIndex(2)
        self.money12.clear()
    #현금 입금확인
    def money1(self):
        aa = self.money12.text()
        if aa.isdigit():
            a = int(aa)
            b = int(self.totalprice)
            if a > b:
                QMessageBox.information(self, '결제성공', f"거스름돈 {str(a - b)}원 입니다.")
                self.stackedWidget_3.setCurrentIndex(3)
            elif a == b:
                QMessageBox.information(self, '결제성공', "    금액이 일치합니다.   ")
                self.stackedWidget_3.setCurrentIndex(3)
            else:
                QMessageBox.warning(self, '금액부족', "금액이 반환됩니다 다시 넣어주세요")
                self.money12.clear()
        else:
            QMessageBox.warning(self, '경고', "현금을 입금해주세요")
            self.money12.clear()



    #카드삽입 화면 이동
    def menu4(self):
        self.stackedWidget_3.setCurrentIndex(6)
    #카드 결제중 화면 이동
    def menu5(self):
        self.stackedWidget_3.setCurrentIndex(5)
        global cnt
        cnt = 5
        self.timelabel.setText(str(5))
        self.menu6()
    def menu6(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.end2)
        self.timer.start(1000)
    #카드 결제 끝 결제완료화면이동
    def end2(self):
        global cnt
        cnt -= 1
        self.timelabel.setText(str(cnt))
        if cnt == -1 :
            self.timer.stop()
            self.stackedWidget.setCurrentIndex(4)
            self.total.clear()
            self.order.clear()
            self.order2.clear()
            self.count = 0
            self.totalprice = 0
            self.menuss = {}
    #관리자 로그인 확인
    def login(self):
        pw = self.userpw.text()
        with open("id",'r') as file:
            id = file.read()
        if pw == id :
            QMessageBox.information(self,"로그인 성공","로그인 성공하였습니다.")
            self.stackedWidget_4.setCurrentIndex(1)
            self.userpw.clear()
        else:
            QMessageBox.warning(self,"로그인 실패","패스워드를 다시 입력해주세요")
            self.userpw.clear()


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()


    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()