### Environment Requirements

#### **JDK**

JDK 版本：jdk-17.0.3.7

下载链接：https://www.oracle.com/cn/java/technologies/downloads/

#### Android Studio 和 Android SDK

Android SDK 版本：Android-13.0（通过 Android Studio 安装）

下载链接：https://developer.android.google.cn/studio

#### Appium Server

#### 模拟器

模拟器名称：雷电模拟器 

连接本机：127.0.0.1

端口：5555

下载链接：https://www.ldmnq.com/

```
npm install -g appium
npm install appium-doctor -g
pip install Appium-Python-Client
```



Appium 是一个用 Node.js 写的、暴露 REST API 的 WEB 服务器。它接受来自客户端的连接，监听命令并在移动设备上执行，答复 HTTP 响应来描述执行结果。

## 方法记录

在雷电模拟器中打开京东 APP 后，在命令行中输入 `adb shell dumpsys window | findstr mCurrentFocus`， 获取 appPackage 和 appActivity。

京东 APP 的获取结果：

 mCurrentFocus=Window{9d7ba84 u0 com.jingdong.app.mall/com.jingdong.app.mall.MainFrameActivity}

得到

appPackage 是 com.jingdong.app.mall

appActivity 是 com.jingdong.app.mall.MainFrameActivity



com.bilibili.fatego

com.bilibili.fatego.UnityPlayerNativeActivity



#### bilibili登录记录

  mCurrentFocus=Window{4263b35 u0 tv.danmaku.bili/tv.danmaku.bili.MainActivityV2}

 tv.danmaku.bili/tv.danmaku.bili.MainActivityV2

“同意并继续”按钮 tv.danmaku.bili:id/agree

搜索栏 tv.danmaku.bili:id/expand_search





在开启python脚本之前要运行这个开启appppppium

appium -a localhost -p 4723





An unknown server-side error occurred while processing the command. Original error: Error occured while starting App. Original error: Error executing adbExec. Original error: 'Command 'C\:\\Users\\11678\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb.exe -P 5037 -s emulator-5554 shell am start -W -n com.jingdong.app.mall/com.jingdong.app.mall.MainFrameActivity -S' exited with code 255'; Stderr: 'Security exception: Permission Denial: starting Intent { flg=0x10000000 cmp=com.jingdong.app.mall/.MainFrameActivity } from null (pid=12064, uid=2000) not exported from uid 10051  java.lang.SecurityException: Permission Denial: starting Intent { flg=0x10000000 cmp=com.jingdong.app.mall/.MainFrameActivity } from null (pid=12064, uid=2000) not exported from uid 10051 at com.android.server.am.ActivityStackSupervisor.checkStartAnyActivityPermission(ActivityStackSupervisor.java:1779) at com.android.server.am.ActivityStarter.startActivity(ActivityStarter.java:725) at com.android.server.am.ActivityStarter.startActivity(ActivityStarter.java:551) at com.android.server.am.ActivityStarter.startActivityMayWait(ActivityStarter.java:1156) at com.android.server.am.ActivityStarter.execute(ActivityStarter.java:490) at com.android.server.am.ActivityManagerService.startActivityAndWait(ActivityManagerService.java:5324) at com.android.server.am.ActivityManagerShellCommand.runStartActivity(ActivityManagerShellCommand.java:474) at com.android.server.am.ActivityManagerShellCommand.onCommand(ActivityManagerShellCommand.java:161) at android.os.ShellCommand.exec(ShellCommand.java:103) at com.android.server.am.ActivityManagerService.onShellCommand(ActivityManagerService.java:16238) at android.os.Binder.shellCommand(Binder.java:634) at android.os.Binder.onTransact(Binder.java:532) at android.app.IActivityManager$Stub.onTransact(IActivityManager.java:3593) at com.android.server.am.ActivityManagerService.onTransact(ActivityManagerService.java:3308) at android.os.Binder.execTransact(Binder.java:731)'; Code: '255'



### APPID

会员购按钮

```
xpath:	//android.widget.FrameLayout[@content-desc="会员购,5之4,标签"]
```

会员购搜索栏

```
id:		tv.danmaku.bili:id/mall_home_search_v2_layout
xpath: 	
```

会员购输入框

```
id:		search_edit
```





```python
# inputTag = driver.find_element_by_id("value")  # 利用ID查找
# 改为：
inputTag = driver.find_element(By.ID, "value")

# inputTags = driver.find_element_by_class_name("value")  # 利用类名查找
# 改为：
inputTag = driver.find_element(By.CLASS_NAME, "value")

# inputTag = driver.find_element_by_name("value")  # 利用name属性查找
# 改为：
inputTag = driver.find_element(By.NAME, "value")

# inputTag = driver.find_element_by_tag_name("value")  # 利用标签名查找
# 改为：
inputTag = driver.find_element(By.TAG_NAME, "value")

# inputTag = driver.find_element_by_xpath("value")  # 利用xpath查找
# 改为：
inputTag = driver.find_element(By.XPATH, "value")

# inputTag = driver.find_element_by_css_selector("value")  # 利用CSS选择器查找
# 改为：
inputTag = driver.find_element(By.CSS_SELETOR, "value")

```

