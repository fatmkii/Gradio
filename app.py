import gradio as gr
import os
from ultralytics import YOLO



css = '''
.contain {
    display: flex;
    justify-content: center;
    align-items: center;
}
#component-0 {
    max-width: 600px;
}
'''

YoloV8  = YOLO('./models/yolov8_otters_epoch400_230503.pt')  # 从yolov8迁移训练的

def YoloV8_handle(image):

    results = YoloV8.predict(image,conf=0.6)
    
    result_plotted = results[0].plot() #numpy的array类型，并且颜色顺序是BGR
    result_cls_list = results[0].boxes.cls.tolist()
    text = ['# 找到了海獭！','# 找到了水獭！','# 没有找到海獭水獭……']
    if(len(result_cls_list)>0):
        result_cls = text[int(result_cls_list[0])]
    else:
        result_cls = text[-1]

    return result_cls,result_plotted

def clear(*args):
    return [None for _ in args]


with gr.Blocks(title='是海獭不是水獭',css=css) as demo:
    gr.Markdown("# 海獭和水獭是不同的，和水獭")
    with gr.Tab("YoloV8"):
        image_1 = gr.Image(type='numpy').style(height=600)
        text_output_1 = gr.Markdown()
        output_1 = [text_output_1,image_1]
        with gr.Row():
            button_clear = gr.Button("清空",variant="secondary")
            button_1 = gr.Button("提交",variant="primary")


        gr.Examples(
        examples=[os.path.join(os.path.dirname(__file__), "examples/sea_otter.jpg"),
                  os.path.join(os.path.dirname(__file__), "examples/river_otter.jpg")],
        inputs=image_1,
        )


    button_1.click(YoloV8_handle, inputs=image_1, outputs=output_1)
    button_clear.click(clear, inputs=[image_1,text_output_1], outputs=[image_1,text_output_1])

demo.launch(
    show_api=False,
    show_error=True,
    server_port=17860)