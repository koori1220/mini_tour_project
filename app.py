from flask import Flask, render_template
import folium

app = Flask(__name__)

# ข้อมูลสถานที่ (สามารถเพิ่มหรือแก้ไขพิกัด รูปภาพ และรายละเอียดได้)
tour_spots = [
    {
        "id": 1,
        "name": "จุดศูนย์กลางเมืองกำแพงเพชร",
        "lat": 16.463528629381965,
        "lon": 99.52823841084464,
        "description": "จุดเริ่มต้นการเดินทางในกำแพงเพชร แหล่งรวมความเจริญและประวัติศาสตร์",
        "image": "https://images.unsplash.com/photo-1590393802688-e04e902b70f0?q=80&w=800&auto=format&fit=crop"
    },
    {
        "id": 2,
        "name": "น้ำตกคลองลาน",
        "lat": 16.1287902,
        "lon": 99.2787884,
        "description": "น้ำตกที่สวยงามและยิ่งใหญ่ที่สุดแห่งหนึ่ง เหมาะแก่การพักผ่อนท่ามกลางธรรมชาติ",
        "image": "https://images.unsplash.com/photo-1433838552652-f9a46b332c40?q=80&w=800&auto=format&fit=crop"
    },
    {
        "id": 3,
        "name": "มหาวิทยาลัยราชภัฏกำแพงเพชร",
        "lat": 16.453815789032237, 
        "lon": 99.51417737139418,
        "description": "สถาบันอุดมศึกษาที่สำคัญ ศูนย์รวมแหล่งเรียนรู้ด้านวิทยาศาสตร์และเทคโนโลยี",
        "image": "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?q=80&w=800&auto=format&fit=crop"
    }
    {
        "id": 4,
        "name": "มหาวิทยาลัยราชภัฏกำแพงเพชร",
        "lat": 16.453815789032237, 
        "lon": 99.51417737139418,
        "description": "สถาบันอุดมศึกษาที่สำคัญ ศูนย์รวมแหล่งเรียนรู้ด้านวิทยาศาสตร์และเทคโนโลยี",
        "image": "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?q=80&w=800&auto=format&fit=crop"
    },
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
