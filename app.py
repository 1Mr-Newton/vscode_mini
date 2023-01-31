import math
from flet import *
h = 800
w = 1000
sidebar_w = 80
text_area_width = w - 420

suc = "#66ffffff"
ssc = "#ffffff"
grey = '#2f333d'
dark = '#21252b'
dark500 = '#21252b'
title_bar_color = '#282c34'
text_color = '#636974'
content_area_text_color = "#cccccc"
catoc = "#282c34"
tah = 675


words_list ={
  "red": [
    "and", "as", "assert", "async", "await", 
    "break", "class", "continue", "def", "del", 
    "elif", "else", "except", "False", "finally", 
    "for", "from", "global", "if", "import", 
    "in", "is", "lambda", "None", "nonlocal", 
    "not", "or", "pass", "raise"]

}


def main(page: Page):
  page.vertical_alignment = 'center'
  page.horizontal_alignment = 'center'
  page.window_bgcolor = colors.TRANSPARENT
  page.bgcolor = colors.TRANSPARENT
  page.window_title_bar_hidden = True
  page.window_frameless = True
  page.window_height =h 
  page.window_width = w
  page.fonts = {
      "SF Pro Bold":"fonts/SFProText-Bold.ttf",
      "SF Pro Heavy":"fonts/SFProText-Heavy.ttf",
      "SF Pro HeavyItalic":"fonts/SFProText-HeavyItalic.ttf",
      "SF Pro Light":"fonts/SFProText-Light.ttf",
      "SF Pro Medium":"fonts/SFProText-Medium.ttf",
      "SF Pro Regular":"fonts/SFProText-Regular.ttf",
      "SF Pro Semibold":"fonts/SFProText-Semibold.ttf",
      "SF Pro SemiboldItalic":"fonts/SFProText-SemiboldItalic.ttf",
    }


  def taw():

    txt_a = w - sidebar_w - content_area.width
    return txt_a

  def move_indicator(e: TapEvent):
    code_area.width = 920 if taw() == 720 else 720
    code_area.update()
    if content_area.data == "opened":
      content_area.data = "closed"
      content_area.width = 0
    else:
      content_area.width = 200
      content_area.data = "opened"
    content_area.update()
    y = side_column.controls.index(e.control)
    sliding.animate = animation.Animation(600,AnimationCurve.BOUNCE_OUT)
    sliding.animate_offset  = animation.Animation(600,AnimationCurve.BOUNCE_OUT)
    sliding.offset = transform.Offset(0,y)
    sliding.update()


  def side_btn_hover(e):
    if e.data == 'true':
      e.control.content.color = ssc
    else:  
      e.control.content.color = suc
      pass
    e.control.update()

  def popup(content,msg):
    return PopupMenuButton(
      content=content,
      tooltip=msg,
      width=500,
      items=[
        PopupMenuItem(text='Command Palette...'),
        PopupMenuItem(),
        PopupMenuItem(text="Settings"),
        PopupMenuItem(text="Extensions"),
        PopupMenuItem(),
        PopupMenuItem(text="Keyboard Shortcuts"),
        PopupMenuItem(text="Migrate Keyboard Shortcuts ..."),
        PopupMenuItem(),
        PopupMenuItem(text="Configure User Snippets"),
        PopupMenuItem(),
        PopupMenuItem(text="Color Theme"),
        PopupMenuItem(text="File Icon Theme"),
        PopupMenuItem(text="Product Icon Theme"),
        PopupMenuItem(),
        PopupMenuItem(text="Settings Sync is on"),
        PopupMenuItem(),
        PopupMenuItem(text="Manage Workspace Trust"),
        PopupMenuItem(),
        PopupMenuItem(text="Check for updates"),
        PopupMenuItem(),
      ]
    ) 


  def side_btn():
    return Container(
      on_hover=side_btn_hover,
      on_click=move_indicator,
      margin=margin.only(left=15),
      height=40,width=55,
      content=Image(
        src='assets/icons/code_area.png',scale=1.2,color=suc
      )
    )
  
  def explorer_menu_hover(e):
    if e.data == "true":
      explorer_menu.bgcolor = 'white12'
    else:
      explorer_menu.bgcolor = None
    explorer_menu.update()  

  def format_code(e):
    pass
  def close_code_content(e: TapEvent):
    code_content_tab.visible = False
    code_area.visible = False
    code_area.update()
    code_content_tab.update()

  def close_app(e):
    page.dialog = confirm_dialog
    confirm_dialog.open = True
    page.update()
    # page.window_close()
    # page.window_destroy()

  # page.window_maximized = True
  def min_app(e):
    page.update()

  def max_app(e):
    pass
  

  def yes_click(e):
      page.window_destroy()

  def no_click(e):
      confirm_dialog.open = False
      page.update()



  confirm_dialog = AlertDialog(
        modal=True,
        title=Text("Quitting doesn't fix bugs!\nCome back to work"),
        content=Text("Do you still wanna run away?"),
        actions=[
            ElevatedButton("Yes, I'm lazy!", on_click=yes_click),
            OutlinedButton("No, I want to continue", on_click=no_click),
        ],
        actions_alignment=MainAxisAlignment.END,
    )

  side_button = side_btn()    

  sliding = Container(
              offset=transform.Offset(0,0),
              bgcolor='white',
              height=50,width=3,
              animate=animation.Animation(500,'decelerate'),
              animate_offset=animation.Animation(500,'decelerate'),
            )      
  
  
  side_column = Column(
    horizontal_alignment='center',
    spacing=0,
    controls=[
      Container(
        data='stay_opened',
        on_hover=side_btn_hover,
        on_click=move_indicator,
        margin=margin.only(left=15),
        # bgcolor='blue',
        height=50,width=55,
        content=Image(
          src='assets/icons/code_area.png',scale=1.2,color=suc
        )
      ),
      Container(
        on_hover=side_btn_hover,
        on_click=move_indicator,
        margin=margin.only(left=15),
        # bgcolor='blue',
        height=50,width=55,
        content=Image(
          src='assets/icons/version_control.png',scale=1.2,color=suc
        )
      ),
      Container(
        on_hover=side_btn_hover,
        on_click=move_indicator,
        margin=margin.only(left=15),
        # bgcolor='blue',
        height=50,width=55,
        content=Image(
          src='assets/icons/version_control.png',scale=1.2,color=suc
        )
      ),
      Container(
        on_hover=side_btn_hover,
        on_click=move_indicator,
        margin=margin.only(left=15),
        # bgcolor='blue',
        height=50,width=55,
        content=Image(
          src='assets/icons/version_control.png',scale=1.2,color=suc
        )
      ),
      Container(
        on_hover=side_btn_hover,
        on_click=move_indicator,
        margin=margin.only(left=15),
        # bgcolor='blue',
        height=50,width=55,
        content=Image(
          src='assets/icons/version_control.png',scale=1.2,color=suc
        )
      ),
      Container(
        on_hover=side_btn_hover,
        on_click=move_indicator,
        margin=margin.only(left=15),
        # bgcolor='blue',
        height=50,width=55,
        content=Image(
          src='assets/icons/version_control.png',scale=1.2,color=suc
        )
      ),
      Container(
        on_hover=side_btn_hover,
        on_click=move_indicator,
        margin=margin.only(left=15),
        # bgcolor='blue',
        height=50,width=55,
        content=Image(
          src='assets/icons/version_control.png',scale=1.2,color=suc
        )
      ),
      Container(
        on_hover=side_btn_hover,
        on_click=move_indicator,
        margin=margin.only(left=15),
        # bgcolor='blue',
        height=50,width=55,
        content=Image(
          src='assets/icons/version_control.png',scale=1.2,color=suc
        )
      ),
      Container(
        on_hover=side_btn_hover,
        on_click=move_indicator,
        margin=margin.only(left=15),
        # bgcolor='blue',
        height=50,width=55,
        content=Image(
          src='assets/icons/version_control.png',scale=1.2,color=suc
        )
      ),
      Container(
        on_hover=side_btn_hover,
        on_click=move_indicator,
        margin=margin.only(left=15),
        # bgcolor='blue',
        height=50,width=55,
        content=Image(
          src='assets/icons/version_control.png',scale=1.2,color=suc
        )
      ),
    ]
  ) # sidebar btn
  code = TextField(
            on_submit=lambda _: print('hellow'),
            multiline=True,
            text_style=TextStyle(
              size=18,
              color='#bbbbbb',
              font_family='SF Pro Regular'
            ),
            border=InputBorder.NONE,
            hint_text="Please subscribe to @1mrnewton on youtube for tutorials on flet...",
            hint_style=TextStyle(
              color=text_color,
              font_family='SF Pro Semibold',
              size=14
            ),
            on_change=format_code
          )

  code_area = Container(
    width=690,
    content=Row(
      vertical_alignment='start',
      spacing=0,
      controls=[
        Container(

          content=Column(
            spacing=0,
            alignment='spaceBetween',
            horizontal_alignment='center',
            width=40,
            height=tah,
            scroll='auto',
            controls=[
              Container(
                margin=margin.only(bottom=10),
                border_radius=10,
                content=Container(
                  height=8,
                  width=8,
                  # bgcolor='red',
                  border_radius=10
                ),
              ),
              
            ]
          ),
        ),

        Container(
          padding=padding.only(top=18),
          content=Column(
            width=70,
            height=tah,
            scroll='auto',
            controls=[
              Text(
                '1',
                font_family='SF Pro Semibold',
                size=18,
                color=text_color,
                
              )
            ]
          ),
        ),

        Container(

          padding=padding.only(left=20,right=30),
          expand=True,
          height=tah,

          
          content=code,
        ),
        
        
      ]
    )
  )

                          
  sidebar_column = Column(
    spacing=0,
    alignment='spaceBetween',
    controls=[
      Row(
        alignment='spaceBetween',
        vertical_alignment='start',
        controls=[
          side_column,
          
          Column(
            controls=[
                sliding
              ]
          ), # sidebar btn selected indicator
          
        ]
        
      ), # top sidebar buttons


      Column(
        controls=[
          Container(
            
            on_hover=side_btn_hover,
            margin=margin.only(left=15),
            height=40,width=55,
            content=popup(Icon(icons.PERSON,color=suc,),"Accounts")
          ),


          Container(
            on_hover=side_btn_hover,
            margin=margin.only(left=15),
            height=40,width=55,
            content=popup(Icon(icons.SETTINGS_OUTLINED,color=suc,),'Settings'),
          ),
          
          
        ]
        
      )
    ]
  )

  menu_tabs = Row(

  ) # top menu tabs        

  explorer_menu = Container(
                on_hover=explorer_menu_hover,
                alignment=alignment.center,
                height=25,
                width=25,
                border_radius = 5,
                # bgcolor='white12',
                content=Row(
                  alignment='center',
                  spacing=3,
                  controls=[
                    Container(height=2,width=2,bgcolor='white',border_radius=5),
                    Container(height=2,width=2,bgcolor='white',border_radius=5),
                    Container(height=2,width=2,bgcolor='white',border_radius=5),
                  ]
                )
              )
  code_content_tab =  Container(
                                      padding=padding.only(right=10,left=10),
                                      width=150,
                                      height=40,
                                      bgcolor="#383e4a",
                                      content=Row(
                                        alignment='spaceBetween',
                                        vertical_alignment='center',
                                        controls=[
                                          Row(
                                            spacing=3,
                                            alignment='center',
                                            vertical_alignment='center',
                                            controls=[
                                              Image(
                                            src='assets/icons/python.png',
                                            scale=0.6
                                          ),
                                          Text('app.py'),
                                            ]
                                          ),
                                          IconButton(
                                            icon=icons.CLOSE,
                                            scale=0.7,
                                            on_click=close_code_content
                                          )
                                        ]
                                      )
                                    )
                                                
  content_area = Container(
    data='opened',
    animate=animation.Animation(600,AnimationCurve.BOUNCE_OUT),
    width=200,
    bgcolor=dark,
    content=Column(
      spacing=0,
      controls=[
        Container(
          height=40,
          padding=padding.only(left=20,right=10,top=10,bottom=10),
          content=Row(
            alignment='spaceBetween',
            controls=[
              Text(
                value='EXPLORER',
                color=content_area_text_color
              ),
              explorer_menu,
              
            ]
          )
        ),
        Container(
          height=25,
          width=200,
          bgcolor=catoc,
          content=Row(
            vertical_alignment='center',
            controls=[
              Container(
                content=Image(
                  src='assets/icons/down.png',
                  color=content_area_text_color,
                  scale=0.4,
                )
              ),
              Text(
                value='VSCODE_MINI',
                font_family='SF Pro Semibold',
                size=14,
                color=content_area_text_color,
              )
            ]
          )
        )
      ]

    )
  ) # content area (files and stuffs details dey here)
  

  page.add(
    Container(
      clip_behavior=ClipBehavior.ANTI_ALIAS,
      bgcolor=grey,
      expand=True,
      width=w,
      height=h,
      border_radius=25,
      content=Column(
        spacing=0,

        controls=[
          Container(
            padding=padding.only(right=20),
            bgcolor=title_bar_color,
            content=Row(
              alignment='spaceBetween',
              height=40,
              controls=[
                Container(
                  alignment=alignment.center,
                  height=40,
                  width=50,
                  image_src='assets/icons/logo.png',
                  scale=0.8
                ),             # vscode icon

                menu_tabs,                   # menu tabs

                Container(
                    # bgcolor='blue',
                    content=WindowDragArea(
                    height=30,
                    width=850,
                    # expand=True,
                    content=Container(
                      alignment=alignment.center,
                      content=Text(
                        value='Visual Studio Code X',
                        font_family='SF Pro Regular',
                        size=16,
                        color=text_color,

                      )
                    ),
                  ),
                ),             # window drag area

                Container(
                  # padding=padding.only(right=30),
                  # bgcolor='green',
                  content=Row(
                    width=100,
                    controls=[
                      Container(
                        on_click=close_app,
                        height=10,
                        width=10,
                        bgcolor='red',
                        border_radius=20
                      ),
                      Container(
                        on_click=min_app,
                        height=10,
                        width=10,
                        bgcolor='orange',
                        border_radius=20
                      ),
                      Container(
                        on_click=max_app,
                        height=10,
                        width=10,
                        bgcolor='green',
                        border_radius=20
                      ),

                    ]
                  ) 
                ),                   # open close minimize maximize buttons

            ]
            ),
          
          ),  # main window toolbar and stuff, window drag area close btn

          Container(
            expand=True,
            content=Row(
              spacing=0,
              controls=[
                Container(
                  padding=padding.only(top=80,bottom=30),
                  width=sidebar_w,
                  bgcolor=grey,
                  content=sidebar_column,
                ), # sidebar

                Container(
                  expand=True,
                  bgcolor=grey,
                  content=Row(
                    spacing = 0,
                    controls=[
                      content_area, # content area (files and stuffs details dey here)
                      Container(
                        content=Column(
                          spacing = 0,
                          controls=[
                            Container(
                              height=40,
                              width=w,
                              bgcolor=dark500,
                              content=Container(
                                content=Row(
                                  controls=[
                                   code_content_tab,
                                  
                                  ]
                                )
                              )
                            ),
                            
                            Container(
                              height=25,
                              width=w,
                              bgcolor=catoc,
                            ),
                            code_area
                          ]
                        )

                      )
                    ]
                  )
                ), # main body
              ]
            )
          )
        ]

      )
    )
  )


app(target=main,assets_dir='assets')