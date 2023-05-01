# App UI 自动化测试

## Environment Requirements

### Anaconda

实验环境由Anaconda进行版本管理。

版本：conda 22.9.0

下载链接：https://www.anaconda.com/download/

### Python

实验中使用Python编写代码，利用Python自带的单元测试库Unittest进行测试。

版本：Python 3.10.10

本实验中的Python利用Anaconda进行下载和管理，如需单独下载可以访问

https://www.python.org/downloads/release/python-31010/

### 雷电模拟器

实验中采用雷电模拟器模拟安卓手机系统进行测试。

系统版本：Android 9

雷电模拟器版本：9.0.43

下载链接：https://www.ldmnq.com/

### Android JDK

实验中使用Android SDK 辅助模拟器与Appium通信，控制App。

版本：Android-13.0（通过 Android Studio 安装）

下载链接：https://developer.android.google.cn/studio

### Appium

实验中使用Appium控制模拟器和测试端口进行测试。

版本：1.22.3

通过以下命令分别安装 Appium、Appium-doctor和Appium-Python-Client：

```
npm install -g appium
npm install appium-doctor -g
pip install Appium-Python-Client
```

Appium 桌面版的下载链接为：https://github.com/appium/appiumdesktop/releases/tag/v1.3.1

Appium 是一个用 Node.js 写的、暴露 REST API 的 WEB 服务器。它接受来自客户端的连接，监听命令并在移动设备上执行，答复 HTTP 响应来描述执行结果。

## 方法记录

###  获取设备和App基本信息

通过Appium启动App，需要在Appium中指定设备相关信息和应用相关信息。需要获取的信息包括操作系统、设备名、设备系统版本号、App包名和App主活动。

我们使用雷电模拟器在设备内的 “设置” 界面查找相关设备信息，可以得到操作系统为Android系统，操作系统版本为Andriod 9。

再使用adb获取设备名，使用命令行命令adb devices获取到目前连接的所有设备，如下图的设备信息，雷电模拟器的设备名为emulator-5554 device。

此外，还需要获取我们所要运行的App对应的包名与主活动名。首先需要在模拟器中运行对应应用，进入应用主界面（这里以Bilibili作为示例），在模拟器所在目录下使用命令行命令 adb shell dumpsys window | findstr mCurrentFocus，得到两个参数

```
appPackage = "tv.danmaku.bili"
appActivity = "tv.danmaku.bili.MainActivityV2"
```

###  获取App交互按钮信息

为使后续实验中能够在Python脚本内控制App的各个控件，需要首先获取各个控件的id等相关信息。本实验使用Appium桌面版连接模拟器获取相关信息。
    
首先打开Appium桌面版，在设置相关信息的位置按操作系统名（platformName），设备系统版本号（platformVersion），设备名（deviceName），App包名（appPackage），App主活动名（appActivity）进行设置后，开启连接，模拟器会自动启动设定好的App并进入到主界面。以下是用于设置参数的json代码：
```
    {
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "emulator-5554 device",
        "appPackage": "tv.danmaku.bili",
        "appActivity": "tv.danmaku.bili.MainActivityV2"
    }
```
进入Appium桌面版的界面后，通过点击界面上相应的元素即可获得客户端元素的ID、xpath、ClassName以及继承关系等信息。

###  使用Python连接Appium控制模拟器

在 Python 脚本中调用os库可以使用系统命令，因此我们在Python中使用如下代码：先将可能正在后台运行的server端清除，以避免不必要的错误；然后打开appium，让appium使用4723端口。

```python
os.system('adb kill-server')
os.system('appium -a localhost -p 4723')
```

此外，由于os.system( )会将未完成的系统调用阻塞，所以我们需要引入多线程机制，将appium挂载在后台进程，而在另一个线程中进行模块测试。 

###  App的初始化和启动

我们将Bilibili的driver控制端和实验中需要用到的控制函数封装为BiliOperator类，通过以下代码对driver端进行参数设置，并启动Bilibili客户端。

```python
    self.desired_caps = {}
    self.desired_caps["platformName"] = "Android"
    self.desired_caps["platformVersion"] = "9"
    self.desired_caps["deviceName"] = "emulator-5554 device"
    self.desired_caps["appPackage"] = "tv.danmaku.bili"
    self.desired_caps["appActivity"] = "tv.danmaku.bili.MainActivityV2"
    self.desired_caps["unicodeKeyboard"] = True
    self.desired_caps["resetKeyboard"] = True
    self.desired_caps["noReset"] = True
    self.desired_caps["newCommandTimeout"] = 100000
    self.host = '127.0.0.1'
    self.port = 4723
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
```

### 使用Unittest自动化测试

我们将控制App的类封装好后，使用一个类继承unittest的TestCase类，在其中设置不同的测试调用相应的控制App的类的方法，从而利用unittest进行自动化测试。

类的继承代码为：
`class TestCalculator(unittest.TestCase):`
    
在测试中用到的部分断言：
`self.assertNotEqual(len(titles), 0)`
`self.assertNotEqual(len(descs), 0)`

并在测试开始后，使用下面代码，运行unittest：
`unittest.main()`

###  测试搜索功能

在实验中，我们准备了一些关键词（如China Daily、SpaceX等），并遍历这些关键词进行搜索。此外，我们还通过桌面版Appium的Inspector窗口，提前获取了实验中所需元素的ID、xpath等属性。我们首先通过driver.find_element选中搜索框，并且获取到搜索框的元素。通过向获取到的搜索框元素发送关键词本文，实现搜索框的输入，然后调用安卓键盘的回车键，开始搜索。进入搜索结果界面后，通过driver.find_elements获得所有ID含有title的元素，遍历这些元素并且获取它们的text属性，从而获得搜索到的所有视频的标题。

```python
    sbox = self.driver.find_element(By.ID, ('search_src_text'))
    sbox.send_keys(keyword)
    time.sleep(1)
    self.driver.press_keycode(AndroidKey.ENTER)
    time.sleep(3)
    eles = self.driver.find_elements(By.ID, 'title')
    for ele in eles:
        titles.append(ele.text)
    time.sleep(15)
```

由于driver端只进行发送信号的工作，并不会检查server端对App操作的完成情况，因此在每次driver的操作后，都需要让进程阻塞一段时间，使得Appium对于App界面的屏幕操作（如点击等）、键盘操作（如回车等）和抓取操作能够充分完成。

### 测试点赞功能

由以下代码实现点赞按钮的获取和点击：

```python
    self.driver.find_element(By.ID, ('frame_recommend')).click()
    time.sleep(1)
```

###  测试评论功能

我们获取评论界面所有ClassName为TextView的元素，然后对元素进行处理和筛选，得到相应视频的评论区中已经加载出的评论。抓取和处理评论的代码如下：

```python
    self.driver.find_element(By.ID, ('tab_sub_title')).click()
    time.sleep(1)
    desctext = self.driver.find_elements(By.CLASS_NAME, ('android.widget.TextView'))
    foundcmt = False
    for desc in desctext:
        if not foundcmt:
            if ":" in desc.text:
                foundcmt = True
            else:
                continue
        if len(desc.text) < 5:
            continue
           descs.append(desc.text)
    time.sleep(3)
```

###  测试会员购搜索和添加购物车功能

除了对Bilibili的视频相关功能进行测试，我们还对Bilibili客户端的购物功能进行了自动化测试。首先用driver.press_keycode(AndroidKey.BACK)模拟安卓机器的回退，回退至主界面后转移到Bilibili会员购界面。进入会员购界面后，通过点击搜索框并使用send_keys(keyword)发送搜索信息，进入商品的搜索结果界面（注意，在此处不能使用 driver.press_keycode(AndroidKey.ENTER)，经测试Bilibili客户端在会员购界面不能相应回车键）。随后，我们任意制定了一个商品的序号，选中进入。最后，通过筛选元素的方式找到购物车按钮，将该商品添加至购物车。

会员购搜索、选择商品和添加购物车的测试代码如下：

```python
    print("Searching for " + keyword + "...")
    sbox = self.driver.find_element(By.ID, ('search_edit'))
    sbox.send_keys(keyword)
    time.sleep(6)
    self.driver.find_element(By.ID, ('mall_id_search_page_actionbar_commit')).click()
    time.sleep(10)
    self.driver.find_elements(By.CLASS_NAME, ('android.webkit.WebView'))
    time.sleep(10)
    eles = self.driver.find_elements(By.CLASS_NAME, ('android.widget.Image'))
    eles[4].click()
    time.sleep(8)
    eles = self.driver.find_elements(By.CLASS_NAME, ('android.view.View'))
    for ele in eles:
        if u"购物车" in ele.text:
            ele.click()
            break
    time.sleep(5)
    self.driver.press_keycode(AndroidKey.BACK)
    time.sleep(1)
    self.driver.press_keycode(AndroidKey.BACK)
    time.sleep(1)
    self.quit_search()
    self.quit_buy()
```

### 异常情况处理功能

在使用Bilibili客户端的过程中，可能会随机弹出很多界面。我们的App自动化测试脚本具有对于这种异常功能的容错能力，比如对于进入界面时弹出的青少年模式选项的处理代码如下：
```python
    try:
        iknow = self.driver.find_element_by_id('text2')
        if iknow:
           iknow = self.driver.find_element_by_id('button')
           print('Adolescent protect found!')
        iknow.click()
    except:
        print('Adolescent protect not found!')
```
通过在App启动时运行上述代码，使得自动化测试脚本不会因为选择青少年模式的弹窗而受到影响。

## 4.6 实验中的问题和解决方式

实验中，由于App本身功能复杂，我们在自动测试过程中遇到了一些问题，并采用了灵活高效的方式解决。

除了上述提到的青少年模式，Bilibili客户端在进入会员购页面是还会概率性展示一个广告页面，阻碍Appium找到所需的页面元素（存在遮挡）。我们观察到,该广告并没有退出按键，但该广告页面会自动在几秒后消失，因此选择在点击会员购按钮进入会员购分区后先等待数秒，再进行搜索操作，这样就能避免该广告页面带来的影响。

对于会员购，我们遇到的另一个问题是在进入搜索结果界面后，一直无法访问到界面元素导致退出。经过大量的实验，我们发现无论加载时间有多长、或是反复退出重进，都会有一个类名为WebView的List对象阻碍我们的脚本获取页面元素，因此我们使用`self.driver.find_elements(By.CLASS_NAME, ('android.webkit.WebView'))`这一段代码简单地对 WebView 类对象进行一次访问，使得它自动退出。

此外，我们还注意到，由于搜索功能需要访问互联网（无论是搜索视频还是搜索会员购商品），需要不定的加载时间，我们本来计划使用try关键字忙等访问，但后来发现由于访问页面元素本身较慢，以及Python调用Appium的调用情况，这样会大幅拖慢程序运行，我们采用两种方式解决：1.部分页面加载所需时间固定，采用忙等的方式，直接阻塞进程等待页面加载；2.对于加载时间不定的页面，采取等待反馈的方式，代码如下，其中func为任意反馈函数（可以是Lambda表达式）：

```python
    def wait(self, func, time=10):
        res = WebDriverWait(self.driver, timeout=time).until(func)
        return res
```
