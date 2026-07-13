from flask import Flask, render_template
import folium

app = Flask(__name__)

# ข้อมูลสถานที่ (สามารถเพิ่มหรือแก้ไขพิกัด รูปภาพ และรายละเอียดได้)
tour_spots = [
    {
        "id": 1,
        "name": "ศาลหลักเมืองกำแพงเพชร",
        "lat": 16.49052155547407, 
        "lon": 99.51596786992796,
        "description": "จุดเริ่มต้นการเดินทางในกำแพงเพชร แหล่งรวมความเจริญและประวัติศาสตร์",
        "image": "http://lh3.googleusercontent.com/gps-cs-s/APNQkAEKMllqGFSek3J7oOjxZbZZlvULkcRHYC4SsNXrKVe7xvtfZjTKtW69JTRaPx3Rmry1el0PVc198Iror06y5bsy2-CvkrF86e44_Dtpd_7LtQDltJM2dzLxut9FpKSCKo3qCyefmz37_9U-=w408-h544-k-no"
    },
    {
        "id": 2,
        "name": "น้ำตกคลองลาน",
        "lat": 16.1298085014545, 
        "lon": 99.27469516897443,
        "description": "น้ำตกที่สวยงามและยิ่งใหญ่ที่สุดแห่งหนึ่ง เหมาะแก่การพักผ่อนท่ามกลางธรรมชาติ",
        "image": "https://lh3.googleusercontent.com/gps-cs-s/APNQkAGmg73ee71MnnRuKUaCRkxEsoi7RFx4Du9AIA6wtxCrBU0h-tpVma76pEAqFcs7AsCMj4s0W0JspaNKkwb4BG0UxzG3s5up2Q0EvI28HOhyNs0LSV20NTMK-kmAqiJTjf7yX5om=w408-h306-k-no"
    },
    {
        "id": 3,
        "name": "มหาวิทยาลัยราชภัฏกำแพงเพชร",
        "lat": 16.453815789032237, 
        "lon": 99.51417737139418,
        "description": "สถาบันอุดมศึกษาที่สำคัญ ศูนย์รวมแหล่งเรียนรู้ด้านวิทยาศาสตร์และเทคโนโลยี",
        "image": "https://reg.kpru.ac.th/th/data/base/regnow.jpg"
    },
    {
        "id": 4,
        "name": "ชาใจ Story",
        "lat": 16.459532618747705,  
        "lon": 99.51768742470426,
        "description": "สถานที่พักผ่อน กินชาเย็นๆ",
        "image": "https://lh3.googleusercontent.com/gps-cs-s/APNQkAFKaJzr-Ry3bv-HhEx3Q5jN-Ieg73vxqOMBrij8ly1J8dg3x9mzpteU6sSUqk_8TzgiyD9GUwAwVvJnTV3awPeKHh0NcAQA56BZAoo3YVI3-WALNr1VYGDFWTYd4O5VbhyaIZASMYka6ag=w408-h544-k-no"
    },
    {
        "id": 5,
        "name": "คิริมัสสึชาบู สาขากำแพงเพชร",
        "lat": 16.449602797122367,   
        "lon": 99.50894365236901,
        "description": "ร้านชาบูปิ้งอย่าง",
        "image": "https://lh3.googleusercontent.com/gps-cs-s/APNQkAG1N1axSVo3rxt8AEwjFtKhQgCqllvETEwbPP9CQGgFixFiIvyj6PYAUaNnwg1O29KH5BDjIoE1MWnorux_3z4tVqzKHa8ppKuCrPZuOgbgkc4dW5ORWOsXbgo5GKRBBPuLkw51NeNByYdH=w408-h306-k-no"
    }
]

@app.route('/')
def index():
    # 1. กำหนดพิกัดเริ่มต้นของแผนที่ (ใช้พิกัดที่ให้มาเป็นจุดศูนย์กลาง)
    start_coords = [16.463528629381965, 99.52823841084464]
    
    # 2. สร้างแผนที่ Folium
    m = folium.Map(location=start_coords, zoom_start=10)

    # 3. วนลูปเพื่อปักหมุด (Marker) สถานที่ต่างๆ ลงบนแผนที่
    for spot in tour_spots:
        folium.Marker(
            location=[spot['lat'], spot['lon']],
            popup=f"<b style='font-family:kanit;'>{spot['name']}</b>",
            tooltip="คลิกเพื่อดูชื่อสถานที่",
            icon=folium.Icon(color="teal", icon="info-sign")
        ).add_to(m)

    # 4. ดึงโค้ด HTML ของแผนที่เพื่อนำไปฝังในหน้าเว็บ
    map_html = m._repr_html_()

    return render_template('index.html', map_html=map_html, spots=tour_spots)

if __name__ == '__main__':
    # สำหรับรันทดสอบในเครื่อง
    app.run(debug=True)
