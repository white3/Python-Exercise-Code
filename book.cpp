#include <iostream>
#include <conio.h> //控制台数据输入输出的函数
#include <fstream> //文件流
#include <iomanip> //控制数据输出格式
#include <cstring>
#include <stdlib.h>
using namespace std;
const int Maxr = 100; //最多的读者数
const int Maxb = 100; //最多的图书数
const int Maxbor = 5; //每位读者最多借的书
class Book
{ //图书类，实现对图书的描述，图书的编号，书名，借出，还入等功能
private:
  int tag;          //删除标记 1:已删 0:未删
  int no;           //图书编号
  char name[20];    //书名
  char author[20];  //作者
  char fenlei[20];  //分类号
  char cbs[20];     //出版社
  int cbtime;       //出版时间
  double bookprice; //图书价格
  int onshelf;      //是否再架 1:再架 2:已借
public:
  Book() { ; }
  char *getname()
  { //获取书名
    return name;
  }
  char *getauthorname()
  { //获取作者名
    return author;
  }

  char *getfenlei()
  { //获取分类号
    return fenlei;
  }
  char *getcbsname()
  { //获取出版社名
    return cbs;
  }
  int getcbtime()
  { //获取出版时间
    return cbtime;
  }
  double getbookprice()
  { //获取图书价格
    return bookprice;
  }
  int getno()
  { //获取图书编号
    return no;
  }
  int gettag()
  { //获取删除标记
    return tag;
  }
  void setname(char na[])
  { //设置书名
    strcpy(name, na);
  }
  void setauthorname(char aa[])
  { //设置作者名
    strcpy(author, aa);
  }
  void setfenlei(char fe[])
  { //设置分类号
    strcpy(fenlei, fe);
  }
  void setcbs(char ca[])
  { //设置出版社
    strcpy(cbs, ca);
  }
  void setcbtime(int time)
  { //设置时间
    cbtime = time;
  }
  void setbookprice(double price)
  { //设置图书价格
    bookprice = price;
  }
  void setonshelf(int oa)
  {
    onshelf = oa;
  }
  void delbook()
  { //删除图书
    char i;
    cout << "确定删除吗？Y/N ?" << endl;
    cin >> i;
    if (i == 'y' || i == 'Y')
      tag = 1;
  }
  void addbook(int n, char *na, char *aa, char *fe, char *ca, int time, double price, int oa)
  { //增加图书
    tag = 0;
    no = n;
    strcpy(name, na);
    strcpy(author, aa);
    strcpy(cbs, ca);
    strcpy(fenlei, fe);
    cbtime = time;
    bookprice = price;
    onshelf = oa;
  }
  int borrowbook()
  { //借书操作
    if (onshelf > 0)
    {
      onshelf--;
      return 1;
    }
    return 0;
  }
  void retbook()
  { //还书操作
    onshelf++;
  }
  void disp()
  { //输出图书
    cout << setw(3) << no << setw(10) << name << setw(10) << author << setw(10) << fenlei << setw(15) << cbs << setw(10) << cbtime << setw(10) << bookprice << setw(10) << onshelf << endl;
  }
};

class BDatabase
{ //图书库类，实现对图书的维护，查找，删除等
private:
  int top;         //图书记录指针
  Book book[Maxb]; //图书记录
public:
  BDatabase()
  { //构造函数，将book.txt读到book[]中
    Book b;
    top = -1;
    fstream file("book.txt", ios::in);
    while (1)
    {
      file.read((char *)&b, sizeof(b));
      if (!file)
        break;
      top++;
      book[top] = b;
    }
    file.close();
  }
  void clear()
  { //全删
    char i;
    cout << "确定全部删除吗？Y/N ?" << endl;
    cin >> i;
    if (i == 'y' || i == 'Y')
      top = -1;
  }
  int addbook(int n, char *na, char *aa, char *fe, char *ca, int time, double price, int oa)
  { //增加图书
    Book *p = query1(n);
    if (NULL == p)
    {
      top++;
      book[top].addbook(n, na, aa, fe, ca, time, price, oa);
      return 1;
    }
    return 0;
  }
  Book *query1(int bookid)
  { //按编号查找图书
    for (int i = 0; i <= top; i++)
      if (book[i].getno() == bookid && book[i].gettag() == 0)
      {
        return &book[i];
      }
    return NULL;
  }
  Book *query2(char a[])
  { //按书名查找图书
    Book *e;
    int r = 0;
    for (int i = 0; i <= top; i++)
      if (strcmp(book[i].getname(), a) == 0 && book[i].gettag() == 0)
      {
        if (r == 0)
          cout << setw(3) << "编号" << setw(10) << "书名" << setw(10) << "作者" << setw(10) << "分类号" << setw(15) << "出版社" << setw(10) << "出版时间" << setw(10) << "图书价格" << setw(10) << "存量" << endl;
        e = &book[i];
        e->disp();
        r++;
      }
    if (r == 0)
      cout << "找不到该书!" << endl;
    return NULL;
  }
  Book *query3(char a[])
  { //按作者查找图书
    Book *e;
    int r = 0;
    for (int i = 0; i <= top; i++)
      if (strcmp(book[i].getauthorname(), a) == 0 && book[i].gettag() == 0)
      {
        if (r == 0)
          cout << setw(3) << "编号" << setw(10) << "书名" << setw(10) << "作者" << setw(10) << "分类号" << setw(15) << "出版社" << setw(10) << "出版时间" << setw(10) << "图书价格" << setw(10) << "存量" << endl;
        e = &book[i];
        e->disp();
        r++;
      }
    if (r == 0)
      cout << "找不到该书!" << endl;
    return NULL;
  }
  Book *query4(char a[])
  { //按出版社查找图书
    Book *e;
    int r = 0;
    for (int i = 0; i <= top; i++)
      if (strcmp(book[i].getcbsname(), a) == 0 && book[i].gettag() == 0)
      {
        if (r == 0)
          cout << setw(3) << "编号" << setw(10) << "书名" << setw(10) << "作者" << setw(10) << "分类号" << setw(15) << "出版社" << setw(10) << "出版时间" << setw(10) << "图书价格" << setw(10) << "存量" << endl;
        e = &book[i];
        e->disp();
        r++;
      }
    if (r == 0)
      cout << "找不到该书!" << endl;
    return NULL;
  }
  void bookdata(); //图书库信息
  void disp()
  {
    for (int i = 0; i <= top; i++)
      if (book[i].gettag() == 0)
        book[i].disp();
  }
  ~BDatabase()
  { //析构函数，将book[]写到book.txt文件中
    fstream file("book.txt", ios::out);
    for (int i = 0; i <= top; i++)
      if (book[i].gettag() == 0)
        file.write((char *)&book[i], sizeof(book[i]));
    file.close();
  }
};
void BDatabase::bookdata()
{
  char choice3;
  char bname[40];   //书名
  char auname[40];  //作者名
  char bfenlei[40]; //分类号
  char cname[40];   //出版社
  int time;         //出版时间
  double price;     //价格
  char ch;
  int choice4;
  int bookid;
  int bookod;
  Book *b;
  while (choice3 != '0')
  {
    cout << "\n\t\t\t**  图 书 信 息 **\n"
         << endl;
    cout << "\t\t\t** 1.新    增 **" << endl;
    cout << "\t\t\t** 2.更    改 **" << endl;
    cout << "\t\t\t** 3.删    除 **" << endl;
    cout << "\t\t\t** 4.查    找 **" << endl;
    cout << "\t\t\t** 5.显    示 **" << endl;
    cout << "\t\t\t** 6.全    删 **" << endl;
    cout << "\t\t\t** 0.返    回 **" << endl;
    cout << "\t\t\t 请选择：";
    cin >> choice3;
    switch (choice3)
    {
    case '1':
      cout << "请输入新书编号:";
      cin >> bookid;

      b = query1(bookid);
      if (b != NULL)
      {
        cout << "该编号已经存在，不能添加!" << endl;
        break;
      }
      cout << "请输入新书书名:";
      cin >> bname;
      cout << "请输入新书作者名:";
      cin >> auname;
      cout << "请输入新书分类号:";
      cin >> bfenlei;
      cout << "请输入新书出版社:";
      cin >> cname;
      cout << "请输入新书出版时间:";
      cin >> time;
      cout << "请输入图书价格:";
      cin >> price;

      cout << "请输入新书数量:";
      cin >> bookod;
      addbook(bookid, bname, auname, bfenlei, cname, time, price, bookod);

      char choice2;
      {
        cout << "\n\t\t\t** 是 否 保 存 Y/N ?**\n"
             << endl;
        cout << "\t\t\t** 1. Y 保  存 **" << endl;
        cout << "\t\t\t** 0. N 不  保  存 **" << endl;
        cout << "\t\t\t 请 选 择: ";
        cin >> choice2;
        switch (choice2)
        {
        case '1':

          cout << "添加图书成功!";

          break;
        case '0':

          break;
        }
      }
      getch();
      break;
    case '2':
      cout << "请输入图书编号:";
      cin >> bookid;
      b = query1(bookid);
      if (b == NULL)
      {
        cout << "该图书不存在! " << endl;
        break;
      }
      cout << "该图书的信息是：" << endl;
      cout << setw(3) << "编号" << setw(10) << "书名" << setw(10) << "作者" << setw(10) << "分类号" << setw(15) << "出版社" << setw(10) << "出版时间" << setw(10) << "图书价格" << setw(10) << "存量" << endl;
      b->disp();
      cout << "是否修改?( y/n ):";
      cin >> ch;
      if (ch == 'y' || ch == 'Y')
      {
        int a;
        cout << "\n\t\t\t**  图 书 修 改 **\n"
             << endl;
        cout << "\t\t\t** 1.修 改 书 名   **" << endl;
        cout << "\t\t\t** 2.修 改 作 者   **" << endl;
        cout << "\t\t\t** 3.修 改 分 类 号  **" << endl;
        cout << "\t\t\t** 4.修 改 出 版 社  **" << endl;
        cout << "\t\t\t** 5.修 改 出 版 时 间**" << endl;
        cout << "\t\t\t** 6.修 改 图 书 价 格**" << endl;
        cout << "\t\t\t** 7.修 改 图 书 数 量**" << endl;
        cout << "\t\t\t** 0.返    回 **" << endl;
        cout << "\t\t\t 请选择：";
        cin >> a;
        switch (a)
        {
        case 1:
          cout << "请输入新的书名:";
          cin >> bname;
          b->setname(bname);
          break;
        case 2:
          cout << "请输入新的作者:";
          cin >> auname;
          b->setauthorname(auname);
          break;
        case 3:
          cout << "请输入新的分类号:";
          cin >> bfenlei;
          b->setfenlei(bfenlei);
          break;
        case 4:
          cout << "请输入新书出版社:";
          cin >> cname;
          b->setcbs(cname);
          break;
        case 5:
          cout << "请输入新书出版时间:";
          cin >> time;
          b->setcbtime(time);
          break;
        case 6:
          cout << "请输入图书价格:";
          cin >> price;
          b->setbookprice(price);
          break;
        case 7:
          cout << "请输入新的存量:";
          cin >> bookod;
          b->setonshelf(bookod);
          break;
        case 0:
          break;
        }
      }
      cout << "修改图书成功!";
      getch();
      break;
    case '3':
      cout << "请输入图书编号:";
      cin >> bookid;
      b = query1(bookid);
      if (b == NULL)
      {
        cout << "该图书不存在，无法删除!" << endl;
        break;
      }
      b->delbook();
      cout << "删除成功!";
      getch();
      break;
    case '4':
      cout << "\n\t\t\t** 1.按图书编号查找 **" << endl;
      cout << "\t\t\t** 2.按图书书名查找 **" << endl;
      cout << "\t\t\t** 3.按图书作者查找 **" << endl;
      cout << "\t\t\t** 4.按图书出版社查找**" << endl;
      cout << "\t\t\t** 0. 返   回  **" << endl;
      cout << "\t\t\t 请选择:";
      cin >> choice4;
      switch (choice4)
      {
      case 1:
        cout << "请输入图书编号:";
        cin >> bookid;
        b = query1(bookid);
        if (b == NULL)
        {
          cout << "该图书不存在!";
          break;
        }
        cout << setw(3) << "编号" << setw(10) << "书名" << setw(10) << "作者" << setw(10) << "分类号" << setw(15) << "出版社" << setw(10) << "出版时间" << setw(10) << "图书价格" << setw(10) << "存量" << endl;
        b->disp();
        break;
      case 2:
        cout << "请输入图书书名:";
        cin >> bname;
        b = query2(bname);
        break;
      case 3:
        cout << "请输入图书作者:";
        cin >> auname;
        b = query3(auname);
        break;
      case 4:
        cout << "请输入图书出版社:";
        cin >> cname;
        b = query4(cname);
        break;
      case 0:
        break;
      }
      break;
    case '5':
      cout << setw(3) << "编号" << setw(10) << "书名" << setw(10) << "作者" << setw(10) << "分类号" << setw(15) << "出版社" << setw(10) << "出版时间" << setw(10) << "图书价格" << setw(10) << "存量" << endl;
      disp();
      getch();
      break;
    case '6':
      clear();
      break;
    default:
      break;
    }
  }
}

class Reader
{ //读者的信息描述
private:
  int tag;             //删除标记 1表示已删 0表示未删
  int no;              //读者编号
  char name[20];       //读者姓名
  int borbook[Maxbor]; //所借图书
public:
  Reader() //构造函数
  {
    ;
  }
  friend ostream &operator<<(ostream &output, Reader &rd)
  {
    output << rd.no;
    output << "  ";
    output << endl;
    return output;
  }
  char *getname()
  { //获取姓名
    return name;
  }
  int gettag()
  { //获取删除标记
    return tag;
  }
  int getno()
  { //获取读者编号
    return no;
  }
  void setname(char na[])
  { //设置姓名
    strcpy(name, na);
  }
  void delbook()
  { //设置删除标记 1:已删 0:未删
    char i;
    cout << "确定删除吗？Y/N ?" << endl;
    cin >> i;
    if (i == 'y' || i == 'Y')
      tag = 1;
  }
  void addreader(int n, char *na)
  { //增加读者
    tag = 0;
    no = n;
    strcpy(name, na);
    for (int i = 0; i < Maxbor; i++)
      borbook[i] = 0;
  }
  void borrowbook(int bookid)
  { //借书操作
    for (int i = 0; i < Maxbor; i++)
    {
      if (borbook[i] == 0)
      {
        borbook[i] = bookid;
        return;
      }
    }
  }
  int retbook(int bookid)
  { //还书操作
    for (int i = 0; i < Maxbor; i++)
    {
      if (borbook[i] == bookid)
      {
        borbook[i] = 0;
        cout << "还书成功!" << endl;
        return 1;
      }
    }
    cout << "未借该书，还书失败!" << endl;
    return 0;
  }
  void disp()
  { //读出读者信息
    int have = 0;
    int bz = 0;
    cout << setw(5) << no << setw(21) << name << setw(15);
    for (int i = 0; i < Maxbor; i++)
      if (borbook[i] != 0)
      {
        if (bz == 0)
        {
          have = 1;
          cout << "[" << borbook[i] << "]\t\t" << endl;
          bz++;
        }
        else
        {
          cout << "\r\t\t\t\t\t"
                  "["
               << borbook[i] << "]\t\t" << setw(15) << endl;
        }
      }
    if (have == 0)
      cout << "\t   还未借书" << endl;
  }
};

class RDatabase
{ //读者类库，实现建立读者的个人资料
private:
  int top;           //读者记录指针
  Reader read[Maxr]; //读者记录
public:
  RDatabase()
  { //构造函数，将reader.txt读到read[]中
    Reader s;
    top = -1;
    fstream file("reader.txt", ios::in); //打开一个输入文件
    while (1)
    {
      file.read((char *)&s, sizeof(s));
      if (!file)
        break;
      top++;
      read[top] = s;
    }
    file.close(); //关闭 reader.txt 文件
  }
  void clear()
  { //删除所有读者信息
    char i;
    cout << "确定全部删除吗？Y/N ?" << endl;
    cin >> i;
    if (i == 'y' || i == 'Y')
      top = -1;
  }
  int addreader(int n, char *na)
  { //添加读者时先查找是否存在
    Reader *p = queryid(n);
    if (p == NULL)
    {
      top++;
      read[top].addreader(n, na);
      return 1;
    }
    else
      cout << "该编号已经存在!";
    return 0;
  }
  Reader *queryid(int readerid)
  { //按读者编号查找
    for (int i = 0; i <= top; i++)
      if (read[i].getno() == readerid && read[i].gettag() == 0)
      {
        return &read[i];
      }
    return NULL;
  }
  Reader *queryname(char readername[10])
  { //按读者姓名查找
    for (int i = 0; i <= top; i++)
      if (strcmp(read[i].getname(), readername) == 0 && read[i].gettag() == 0)
      {
        return &read[i];
      }
    return NULL;
  }
  void disp()
  { //输出所有读者信息
    for (int i = 0; i <= top; i++)
      if (read[i].gettag() == 0)
        read[i].disp();
  }
  void readerdata(); //读者库信息
  ~RDatabase()
  { //析构函数，将read[]写到reader.txt文件中
    fstream file("reader.txt", ios::out);
    for (int i = 0; i <= top; i++)
      if (read[i].gettag() == 0)
        file.write((char *)&read[i], sizeof(read[i]));
    file.close();
  }
};

void RDatabase::readerdata()
{
  char choice1;
  char rname[20];
  int readerid;
  char readername[10];
  int choice2;
  Reader *r;
  while (choice1 != '0')
  {
    cout << "\n\t\t\t** 读 者 信 息 **\n"
         << endl;
    cout << "\t\t\t** 1. 新    增 **" << endl;
    cout << "\t\t\t** 2. 更    改 **" << endl;
    cout << "\t\t\t** 3. 删    除 **" << endl;
    cout << "\t\t\t** 4. 查    找 **" << endl;
    cout << "\t\t\t** 5. 显    示 **" << endl;
    cout << "\t\t\t** 6. 全    删 **" << endl;
    cout << "\t\t\t** 0. 返    回 **" << endl;
    cout << "\t\t\t 请选择：";
    cin >> choice1;
    switch (choice1)
    {
    case '1':
      cout << "请输入读者编号:";
      cin >> readerid;
      cout << "请输入读者姓名:";
      cin >> rname;
      addreader(readerid, rname);
      cout << "添加读者成功!" << endl;
      getch();
      break;
    case '2':
      cout << "请输入读者编号:";
      cin >> readerid;
      r = queryid(readerid);
      if (r == NULL)
      {
        cout << "该读者不存在! " << endl;
        break;
      }
      cout << "请输入新的姓名:";
      cin >> rname;
      r->setname(rname);
      cout << "修改读者成功!" << endl;
      getch();
      break;
    case '3':
      cout << "请输入读者编号:";
      cin >> readerid;
      r = queryid(readerid);
      if (r == NULL)
      {
        cout << "该读者不存在!" << endl;
        break;
      }
      r->delbook();
      cout << "删除成功!" << endl;
      getch();
      break;
    case '4':
      cout << "\n\t\t\t** 1.按读者编号查找 **" << endl;
      cout << "\t\t\t** 2.按读者姓名查找 **" << endl;
      cout << "\t\t\t** 0.返     回 **" << endl;
      cout << "\t\t\t 请选择:";
      cin >> choice2;
      switch (choice2)
      {
      case 1:
        cout << "请输入读者编号:";
        cin >> readerid;
        r = queryid(readerid);
        if (r == NULL)
        {
          cout << "该读者不存在!" << endl;
          break;
        }
        cout << setw(10) << "读者编号" << setw(17) << "读者姓名" << setw(20) << "已借书编号" << endl;
        r->disp();
        break;
      case 2:
        cout << "请输入读者姓名:";
        cin >> readername;
        r = queryname(readername);
        if (r == NULL)
        {
          cout << "该读者不存在!" << endl;
          break;
        }
        cout << setw(10) << "读者编号" << setw(17) << "读者姓名" << setw(20) << "已借书编号" << endl;
        r->disp();
        break;
      case 0:
        break;
      }
      break;
    case '5':
      cout << setw(10) << "读者编号" << setw(17) << "读者姓名" << setw(20) << "已借书编号" << endl;
      disp();
      getch();
      break;
    case '6':
      clear();
      break;
    default:
      break;
    }
  }
}

class maindesk //实现程序的主界面
{
  char choice5;
  char choice2;
  double xh, mm;
  int bookid, readerid;
  RDatabase ReaderDB;
  Reader *r;
  BDatabase BookDB;
  Book *b;

public:
  maindesk() { ; }

  int denglu()
  {

    int k = 0;
    cout << "\n\t\t\t 欢 迎 光 临 图 书 馆 管 理 系 统!" << endl;
    cout << "\t\t\t 您 共 有 3 次 登 陆 机 会" << endl;
    while (choice2 != '0')
    {
      ++k;
      cout << "\t\t\t ** 1. 登  录 **" << endl;
      cout << "\t\t\t ** 0. 退  出 **" << endl;
      cout << "\t\t\t 请 选 择:  ";
      cin >> choice2;
      switch (choice2)
      {

      case '1':

        cout << "请输入学号和密码" << endl;
        cin >> xh >> mm;

        if ((xh >= 100000000) && (xh <= 999999999))
        {
          cout << "登录成功" << endl;
          enterdesk();
        }

        if ((xh < 138325039) || (xh > 138325039) || (xh != mm))
        {
          cout << "登录失败：您还有" << 3 - k << "次登陆机会" << endl;
          if (k >= 3)
          {
            cout << "您已超过登录次数上限，系统自动退出!" << endl;
            return 1;
          }
          continue;
        }
        break;

      case '0':
        break;
      }
      return 1;
    }
    return 0;
  }

  void enterdesk()
  {
    while (choice5 != '0')
    {
      system("cls");
      cout << "\n\t\t\t**** 图 书 管 理 系 统****\n\n";
      cout << "\t\t\t** 1.图  书  信  息 **" << endl;
      cout << "\t\t\t** 2.读  者  信  息 **" << endl;
      cout << "\t\t\t** 3.借  阅  图  书 **" << endl;
      cout << "\t\t\t** 4.归  还  图  书 **" << endl;
      cout << "\t\t\t** 0.   退  出   **" << endl;
      cout << "\t\t\t 请选择：";
      cin >> choice5;
      switch (choice5)
      {

      case '1':
      	system("cls");
        BookDB.bookdata();
        break;
      case '2':
      	system("cls");
        ReaderDB.readerdata();
        break;
      case '3':
      	system("cls");
        cout << "\t\t\t\t借书操作" << endl;
        cout << "请输入借书读者编号:";
        cin >> readerid;
        r = ReaderDB.queryid(readerid);
        if (NULL == r)
        { //按编号查找是否有该读者
          cout << "不存在该读者，不能借书!" << endl;
          break;
        }
        cout << "请输入要借图书编号:";
        cin >> bookid;
        b = BookDB.query1(bookid);
        if (b == NULL)
        { //按编号查找是否有该图书
          cout << "不存在该图书，不能借书!" << endl;
          break;
        }
        if (b->borrowbook() == 0)
        {
          cout << "该图书已借完，不能借书!" << endl;
          break;
        }
        cout << "读者借书成功!" << endl;
        r->borrowbook(b->getno());
        break;
      case '4':
      	system("cls");
        cout << "\t\t\t\t还书操作" << endl;
        cout << "请输入还书读者编号:";
        cin >> readerid;
        r = ReaderDB.queryid(readerid);
        if (r == NULL)
        {
          cout << "不存在该读者，不能还书" << endl;
          break;
        }
        cout << "请输入要归还图书编号:";
        cin >> bookid;
        b = BookDB.query1(bookid);
        if (b == NULL)
        {
          cout << "不存在该图书，不能还书" << endl;
          break;
        }
        b->retbook();
        r->retbook(b->getno());
        break;
      case '0':
        break;
      default:

        break;
      }
    }
  }
};

//主函数
int main(int argc, char *argv[])
{
  maindesk yourDesk;
  if (yourDesk.denglu())
    cout << "\t\t 谢 谢 使 用 , 再 见 !" << endl;
  return 0;
}