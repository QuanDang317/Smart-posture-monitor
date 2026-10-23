"""
Script chính: build_full_report.py
Tạo tài liệu Báo cáo Bài tập lớn Smart Posture Monitor V03 hoàn chỉnh, chuẩn học thuật.
Xuất ra 2 định dạng:
1. docs/BAO_CAO_BAI_TAP_LON_SMART_POSTURE_MONITOR.docx (và Desktop)
2. docs/BAO_CAO_BAI_TAP_LON_SMART_POSTURE_MONITOR.md
"""

import os
import sys
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

from report_data import *
from report_appendices import *
from build_helpers import *

sys.stdout.reconfigure(encoding='utf-8')

def build_docx_report():
    print("Bắt đầu khởi tạo tài liệu Word (.docx)...")
    doc = docx.Document()
    
    # 1. Cấu hình trang A4 chuẩn Bộ GD&ĐT / PTIT
    section_cover = doc.sections[0]
    section_cover.page_width = Inches(8.27)   # 21.0 cm
    section_cover.page_height = Inches(11.69) # 29.7 cm
    section_cover.top_margin = Inches(0.79)    # 2.0 cm
    section_cover.bottom_margin = Inches(0.79) # 2.0 cm
    section_cover.left_margin = Inches(1.18)   # 3.0 cm
    section_cover.right_margin = Inches(0.79)  # 2.0 cm
    
    # 2. Trang bìa (Cover Page)
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(0)
    p_inst.paragraph_format.space_after = Pt(2)
    r1 = p_inst.add_run(METADATA["institution"] + "\n")
    r1.font.name = "Times New Roman"
    r1.font.size = Pt(13)
    r1.font.bold = True
    r1.font.color.rgb = RGB_PRIMARY_NAVY
    
    r2 = p_inst.add_run(METADATA["faculty"] + "\n")
    r2.font.name = "Times New Roman"
    r2.font.size = Pt(12)
    r2.font.bold = True
    r2.font.color.rgb = RGB_PRIMARY_NAVY

    r3 = p_inst.add_run(METADATA["department"])
    r3.font.name = "Times New Roman"
    r3.font.size = Pt(12)
    r3.font.bold = True
    r3.font.color.rgb = RGB_SECONDARY_SLATE

    # Đường kẻ ngang tinh tế
    p_line = doc.add_paragraph()
    p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_line.paragraph_format.space_before = Pt(2)
    p_line.paragraph_format.space_after = Pt(14)
    r_l = p_line.add_run("━━━━━━━━━━━━━━━━━━━")
    r_l.font.color.rgb = RGB_PRIMARY_NAVY
    r_l.font.size = Pt(11)

    # Logo PTIT
    logo_path = "docs/extracted_media/image2.jpg"
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(6)
        p_logo.paragraph_format.space_after = Pt(20)
        p_logo.add_run().add_picture(logo_path, width=Inches(1.75))

    # Tên báo cáo
    p_rep = doc.add_paragraph()
    p_rep.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_rep.paragraph_format.space_before = Pt(10)
    p_rep.paragraph_format.space_after = Pt(8)
    r_rep = p_rep.add_run(METADATA["report_type"] + "\n")
    r_rep.font.name = "Times New Roman"
    r_rep.font.size = Pt(18)
    r_rep.font.bold = True
    r_rep.font.color.rgb = RGBColor(160, 20, 20) # Đỏ thẫm truyền thống PTIT
    
    r_sub = p_rep.add_run(f"Học phần: {METADATA['course_name']}")
    r_sub.font.name = "Times New Roman"
    r_sub.font.size = Pt(13)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGB_DARK_GREY

    # Khung tiêu đề Đề tài
    tbl_title = doc.add_table(rows=1, cols=1)
    tbl_title.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_title = tbl_title.cell(0, 0)
    set_cell_background(c_title, "F4F7FB")
    set_cell_margins(c_title, top=160, bottom=160, left=240, right=240)
    set_table_borders(tbl_title, color="1B365D", sz="12")
    
    p_t = c_title.paragraphs[0]
    p_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_t.paragraph_format.space_before = Pt(4)
    p_t.paragraph_format.space_after = Pt(4)
    r_dt = p_t.add_run("ĐỀ TÀI:\n")
    r_dt.font.name = "Times New Roman"
    r_dt.font.size = Pt(14)
    r_dt.font.bold = True
    r_dt.font.color.rgb = RGB_SECONDARY_SLATE
    
    r_title = p_t.add_run(f"“{METADATA['project_title']}”\n")
    r_title.font.name = "Times New Roman"
    r_title.font.size = Pt(18)
    r_title.font.bold = True
    r_title.font.color.rgb = RGB_PRIMARY_NAVY
    
    r_vers = p_t.add_run(f"({METADATA['project_subtitle']})")
    r_vers.font.name = "Times New Roman"
    r_vers.font.size = Pt(12)
    r_vers.font.italic = True
    r_vers.font.color.rgb = RGB_DARK_GREY

    doc.add_paragraph().paragraph_format.space_after = Pt(25)

    # Khung thông tin Giảng viên & Sinh viên
    tbl_meta = doc.add_table(rows=5, cols=2)
    tbl_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r in tbl_meta.rows:
        r.cells[0].width = Inches(2.3)
        r.cells[1].width = Inches(3.7)
        for c in r.cells:
            set_cell_margins(c, top=60, bottom=60, left=80, right=80)
            
    # Bỏ border bảng thông tin
    tblPr = tbl_meta._tbl.tblPr
    tblPr.append(parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="none"/>'
        f'  <w:bottom w:val="none"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideH w:val="none"/>'
        f'  <w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    ))

    def fill_meta_row(row_idx, label, val, bold_val=True):
        p0 = tbl_meta.cell(row_idx, 0).paragraphs[0]
        p0.paragraph_format.space_before = Pt(2)
        p0.paragraph_format.space_after = Pt(2)
        r0 = p0.add_run(label)
        r0.font.name = "Times New Roman"
        r0.font.size = Pt(12.5)
        r0.font.bold = True
        r0.font.color.rgb = RGB_SECONDARY_SLATE
        
        p1 = tbl_meta.cell(row_idx, 1).paragraphs[0]
        p1.paragraph_format.space_before = Pt(2)
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(val)
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(12.5)
        r1.font.bold = bold_val
        r1.font.color.rgb = RGB_TEXT_BLACK

    fill_meta_row(0, "Giảng viên hướng dẫn:", METADATA["instructor"])
    fill_meta_row(1, "Sinh viên thực hiện:", f"1. {METADATA['students'][0]['name']} - {METADATA['students'][0]['code']} ({METADATA['students'][0]['role']})")
    fill_meta_row(2, "", f"2. {METADATA['students'][1]['name']} - {METADATA['students'][1]['code']}")
    fill_meta_row(3, "", f"3. {METADATA['students'][2]['name']} - {METADATA['students'][2]['code']}")
    fill_meta_row(4, "Lớp danh nghĩa:", f"{METADATA['class_name']} - Hệ Đại học chính quy", False)

    doc.add_paragraph().paragraph_format.space_after = Pt(35)

    # Footer bìa: Hà Nội, tháng 10 năm 2026
    p_foot = doc.add_paragraph()
    p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_ft = p_foot.add_run(f"{METADATA['location']}, {METADATA['date']}")
    r_ft.font.name = "Times New Roman"
    r_ft.font.size = Pt(12)
    r_ft.font.bold = True
    r_ft.font.color.rgb = RGB_SECONDARY_SLATE

    # Ngắt trang sang phần nội dung chính
    section_body = doc.add_section(docx.enum.section.WD_SECTION.NEW_PAGE)
    section_body.header_distance = Inches(0.5)
    section_body.footer_distance = Inches(0.5)

    # Thiết lập Header & Footer cho Section Body
    header_p = section_body.header.paragraphs[0]
    header_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_hdr = header_p.add_run("Báo cáo Bài tập lớn: Smart Posture Monitor (V03) | PTIT 2026")
    r_hdr.font.name = "Times New Roman"
    r_hdr.font.size = Pt(9.5)
    r_hdr.font.italic = True
    r_hdr.font.color.rgb = RGBColor(120, 120, 120)

    footer_p = section_body.footer.paragraphs[0]
    footer_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_ft_txt = footer_p.add_run("Học viện Công nghệ Bưu chính Viễn thông  |  Trang ")
    r_ft_txt.font.name = "Times New Roman"
    r_ft_txt.font.size = Pt(9.5)
    r_ft_txt.font.italic = True
    r_ft_txt.font.color.rgb = RGBColor(120, 120, 120)
    
    # Mã trường PAGE tự động của Word
    fldPage = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
    footer_p._p.append(fldPage)

    # =========================================================================
    # LỜI CẢM ƠN & LỜI MỞ ĐẦU
    # =========================================================================
    add_styled_heading(doc, "LỜI CẢM ƠN", level=1)
    add_body_paragraph(doc, "Lời đầu tiên, nhóm sinh viên chúng em xin được bày tỏ lòng biết ơn chân thành và sâu sắc nhất tới thầy ThS. Phạm Danh Tuyên – Giảng viên phụ trách học phần Lập trình Python. Trong suốt quá trình học tập và triển khai đề tài, thầy đã tận tình truyền đạt những kiến thức chuyên môn quý báu, định hướng phương pháp luận nghiên cứu khoa học, đồng thời đưa ra những lời khuyên xác đáng giúp nhóm giải quyết các bài toán kỹ thuật phức tạp từ khâu xử lý ảnh, trích xuất đặc trưng cho đến kiểm thử mô hình học máy theo chuẩn công thái học thực tiễn.")
    add_body_paragraph(doc, "Nhóm cũng xin chân thành cảm ơn các thầy cô giáo trong Khoa Công nghệ Thông tin 1 – Học viện Công nghệ Bưu chính Viễn thông đã tạo điều kiện học tập tốt nhất, cung cấp nền tảng kiến thức vững chắc về lập trình, toán ứng dụng và trí tuệ nhân tạo. Sự đồng hành và động viên của các thầy cô cùng 14 tình nguyện viên tham gia ghi hình xây dựng tập dữ liệu chính là động lực to lớn giúp nhóm hoàn thành đề tài này một cách chỉn chu và trọn vẹn nhất.")
    add_body_paragraph(doc, "Mặc dù đã rất nỗ lực nghiên cứu và hoàn thiện sản phẩm, đề tài chắc chắn khó tránh khỏi những thiếu sót nhất định do giới hạn về mặt thời gian và điều kiện thực nghiệm. Nhóm chúng em rất mong nhận được những nhận xét, góp ý quý báu từ thầy và hội đồng thẩm định để sản phẩm ngày càng hoàn thiện hơn trong tương lai. Kính chúc thầy sức khỏe, niềm vui và luôn gặt hái nhiều thành công trong sự nghiệp trồng người cao quý!", italic=True)

    add_styled_heading(doc, "LỜI MỞ ĐẦU", level=1)
    add_body_paragraph(doc, "Trong kỷ nguyên số hóa và sự phổ biến của mô hình làm việc từ xa (Remote / Hybrid Work), thời gian làm việc và học tập trước màn hình máy tính ngày càng tăng, phổ biến từ 8 đến 12 tiếng mỗi ngày. Tuy nhiên, việc duy trì tư thế ngồi đúng chuẩn công thái học (Ergonomics) trong thời gian dài là một thách thức rất lớn đối với đa số người sử dụng. Người dùng thường vô thức rơi vào các tư thế sai lệch như cúi đầu về phía trước (Forward Head Posture - thường gọi là hội chứng Text Neck), gù lưng và rướn người về phía màn hình (Forward Slouch), hoặc nghiêng người, vẹo cột sống sang một bên (Lateral Lean). Những tư thế sai này nếu kéo dài liên tục không chỉ gây đau mỏi cơ cổ, vai gáy, thắt lưng mà còn làm tăng áp lực lên đĩa đệm cột sống (có thể lên tới 27 kg khi đầu cúi 60°), dẫn tới nguy cơ thoái hóa đốt sống cổ sớm, thoát vị đĩa đệm và suy giảm nghiêm trọng hiệu suất lao động trí tuệ.")
    add_body_paragraph(doc, "Mặc dù nhận thức rõ tầm quan trọng của việc giữ thẳng lưng, người dùng vẫn rất khó tự phát hiện và sửa sai kịp thời, đặc biệt khi đang tập trung cao độ vào công việc chuyên môn. Các giải pháp truyền thống trên thị trường hiện nay bộc lộ nhiều điểm hạn chế: Các thiết bị cảm biến đeo (Wearable IMU Sensors) thường gây vướng víu, khó chịu khi sử dụng cả ngày và đòi hỏi chi phí đầu tư phần cứng; trong khi các phần mềm nhắc giờ cố định (như phương pháp Pomodoro) lại không phản ánh đúng tư thế ngồi thực tế. Do đó, việc xây dựng một hệ thống thị giác thông minh có khả năng giám sát tư thế liên tục, phát hiện sai lệch và đưa ra cảnh báo kịp thời theo thời gian thực là một nhu cầu cấp thiết và mang tính ứng dụng xã hội sâu sắc.")
    add_body_paragraph(doc, "Sự phát triển vượt bậc của Trí tuệ nhân tạo (AI) và Thị giác máy tính (Computer Vision) đã mở ra hướng đi tối ưu cho bài toán này. Bằng cách tận dụng trực tiếp webcam máy tính sẵn có, hệ thống có thể theo dõi tư thế mà không gây cảm giác khó chịu cho người dùng, đồng thời tiết kiệm 100% chi phí mua sắm thiết bị ngoại vi chuyên dụng.")
    add_body_paragraph(doc, "Xuất phát từ thực tiễn trên, nhóm lựa chọn thực hiện đề tài: “Xây dựng hệ thống giám sát tư thế ngồi thời gian thực – Smart Posture Monitor (Phiên bản V03)”. Hệ thống kết hợp giữa mô hình ước lượng tư thế người siêu nhẹ YOLOv8-Pose và thuật toán phân loại Support Vector Machine (SVM nhân RBF), tích hợp cơ chế hiệu chuẩn cá nhân hóa (Personal Baseline Calibration 30 mẫu) và bộ lọc ổn định chuỗi thời gian (Temporal Smoothing, Hysteresis và Yaw Gating). Toàn bộ pipeline được đóng gói thành một ứng dụng Web Dashboard trực quan, vận hành hoàn toàn Offline trên máy trạm cục bộ, bảo vệ quyền riêng tư tuyệt đối cho người dùng.")

    # =========================================================================
    # QUY ƯỚC VÀ THUẬT NGỮ
    # =========================================================================
    add_styled_heading(doc, "QUY ƯỚC VÀ THUẬT NGỮ", level=1)
    add_body_paragraph(doc, "Để bảo đảm tính thống nhất và thuận tiện cho việc theo dõi các nội dung kỹ thuật trong toàn bộ báo cáo, nhóm đưa ra bảng quy ước định nghĩa các thuật ngữ, từ viết tắt và khái niệm chuyên ngành sau đây:")
    
    table_glossary_data = [["Thuật ngữ / Viết tắt", "Định nghĩa và Ý nghĩa sử dụng trong đề tài"]] + GLOSSARY
    create_table_from_data(doc, table_glossary_data, col_widths=[1.8, 4.4], align_center_cols=[0])

    # =========================================================================
    # MỤC LỤC TỔNG THỂ
    # =========================================================================
    add_styled_heading(doc, "MỤC LỤC TỔNG THỂ", level=1)
    
    toc_items = [
        ("LỜI CẢM ƠN", "2"),
        ("LỜI MỞ ĐẦU", "3"),
        ("QUY ƯỚC VÀ THUẬT NGỮ", "4"),
        ("MỤC LỤC TỔNG THỂ", "5"),
        ("DANH MỤC HÌNH VẼ & BẢNG BIỂU", "6"),
        ("CHƯƠNG 1. TỔNG QUAN BÀI TOÁN VÀ MỤC TIÊU", "7"),
        ("  1.1. Bối cảnh và lý do chọn đề tài", "7"),
        ("  1.2. Phát biểu bài toán nhận diện tư thế", "7"),
        ("  1.3. Mục tiêu nghiên cứu và phát triển", "8"),
        ("  1.4. Phạm vi và giới hạn của đề tài", "8"),
        ("CHƯƠNG 2. YÊU CẦU VÀ CHỨC NĂNG HỆ THỐNG", "9"),
        ("  2.1. Yêu cầu chức năng (Functional Requirements)", "9"),
        ("  2.2. Yêu cầu phi chức năng (Non-Functional Requirements)", "11"),
        ("  2.3. Quy trình người dùng (User Flow)", "12"),
        ("CHƯƠNG 3. PHÂN TÍCH VÀ LỰA CHỌN GIẢI PHÁP", "14"),
        ("  3.1. Phân tích các hướng tiếp cận công nghệ", "14"),
        ("  3.2. Kiến trúc giải pháp tổng thể đề xuất", "15"),
        ("  3.3. Ước lượng tư thế và lựa chọn điểm mốc cơ thể (Keypoints)", "17"),
        ("  3.4. Kỹ thuật thiết kế đặc trưng hình học (RAW12)", "20"),
        ("  3.5. Hiệu chuẩn cá nhân hóa và Biểu diễn đặc trưng tương đối (REP13)", "23"),
        ("  3.6. Nghiên cứu và lựa chọn mô hình Machine Learning", "26"),
        ("  3.7. Bộ lọc chuỗi thời gian (Temporal Monitoring & Yaw Gating)", "29"),
        ("CHƯƠNG 4. THIẾT KẾ CHƯƠNG TRÌNH VÀ HỆ THỐNG", "32"),
        ("  4.1. Kiến trúc phân tầng của hệ thống", "32"),
        ("  4.2. Thiết kế chi tiết các module nghiệp vụ", "33"),
        ("  4.3. Thiết kế luồng xử lý thời gian thực (One-Frame-in-Flight)", "35"),
        ("  4.4. Quy trình huấn luyện và kiểm thử mô hình", "37"),
        ("  4.5. Thiết kế giao diện người dùng (Dashboard UI)", "38"),
        ("CHƯƠNG 5. THƯ VIỆN, FRAMEWORK VÀ CÔNG NGHỆ", "42"),
        ("CHƯƠNG 6. THỰC NGHIỆM, KẾT QUẢ VÀ MINH HỌA SẢN PHẨM", "44"),
        ("  6.1. Thu thập và Phân tích tập dữ liệu thực nghiệm (Dataset & EDA)", "44"),
        ("  6.2. Phương pháp đánh giá mô hình (Nested LOPO CV)", "46"),
        ("  6.3. Đánh giá và so sánh hiệu năng các mô hình Machine Learning", "48"),
        ("  6.4. Đánh giá hiệu năng vận hành thời gian thực", "52"),
        ("  6.5. Đánh giá hiệu quả của bộ lọc Temporal Monitoring", "54"),
        ("  6.6. Đánh giá cơ chế thống kê và Điểm Công thái học", "55"),
        ("  6.7. Tổng kết đánh giá ưu điểm và hạn chế của hệ thống", "56"),
        ("CHƯƠNG 7. PHÂN CHIA CÔNG VIỆC TRONG NHÓM", "58"),
        ("CHƯƠNG 8. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN", "60"),
        ("  8.1. Các kết quả chính đạt được", "60"),
        ("  8.2. Những đóng góp nổi bật của đề tài", "60"),
        ("  8.3. Hạn chế và Hướng phát triển tiếp theo", "61"),
        ("CHƯƠNG 9. ỨNG DỤNG AI TRONG QUÁ TRÌNH THỰC HIỆN ĐỀ TÀI", "62"),
        ("TÀI LIỆU THAM KHẢO", "64"),
        ("PHỤ LỤC. THÔNG TIN KỸ THUẬT BỔ SUNG", "65"),
        ("  Phụ lục A. Danh mục chi tiết các đặc trưng hình học (RAW12 & REP13)", "65"),
        ("  Phụ lục B. Cấu hình huấn luyện và không gian tìm kiếm siêu tham số", "68"),
        ("  Phụ lục C. Các đoạn mã nguồn trọng yếu của hệ thống", "70"),
        ("  Phụ lục D. Kết quả thực nghiệm chi tiết từng Fold và từng cá nhân", "75"),
        ("  Phụ lục E. Cấu trúc mã nguồn Repository và Hướng dẫn triển khai", "78")
    ]
    
    tbl_toc = doc.add_table(rows=len(toc_items), cols=2)
    tbl_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r in tbl_toc.rows:
        r.cells[0].width = Inches(5.2)
        r.cells[1].width = Inches(1.0)
        for c in r.cells:
            set_cell_margins(c, top=30, bottom=30, left=40, right=40)
            
    # Bỏ border bảng TOC
    tblPr_toc = tbl_toc._tbl.tblPr
    tblPr_toc.append(parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="none"/>'
        f'  <w:bottom w:val="none"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideH w:val="none"/>'
        f'  <w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    ))
    
    for i, (title, page) in enumerate(toc_items):
        is_chap = title.startswith("CHƯƠNG") or title.startswith("PHỤ LỤC") or title in ["LỜI CẢM ƠN", "LỜI MỞ ĐẦU", "QUY ƯỚC VÀ THUẬT NGỮ", "MỤC LỤC TỔNG THỂ", "DANH MỤC HÌNH VẼ & BẢNG BIỂU", "TÀI LIỆU THAM KHẢO"]
        p0 = tbl_toc.cell(i, 0).paragraphs[0]
        p0.paragraph_format.space_before = Pt(1)
        p0.paragraph_format.space_after = Pt(1)
        r0 = p0.add_run(title)
        r0.font.name = "Times New Roman"
        r0.font.size = Pt(11)
        r0.font.bold = is_chap
        if is_chap:
            r0.font.color.rgb = RGB_PRIMARY_NAVY
            
        p1 = tbl_toc.cell(i, 1).paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p1.paragraph_format.space_before = Pt(1)
        p1.paragraph_format.space_after = Pt(1)
        r1 = p1.add_run(page)
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(11)
        r1.font.bold = is_chap

    # =========================================================================
    # DANH MỤC HÌNH VẼ & BẢNG BIỂU
    # =========================================================================
    add_styled_heading(doc, "DANH MỤC HÌNH VẼ & BẢNG BIỂU", level=1)
    
    add_styled_heading(doc, "Danh mục Hình vẽ", level=2)
    figures_list = [
        "Hình 3.1: Sơ đồ kiến trúc xử lý nhận diện tư thế ngồi đề xuất (Pipeline V03).",
        "Hình 3.2: Minh họa 17 điểm mốc cơ thể theo định dạng COCO của YOLO-Pose.",
        "Hình 3.3: Quy trình hiệu chuẩn Baseline cá nhân hóa và biến đổi RAW12 sang REP13.",
        "Hình 4.1: Sơ đồ kiến trúc tổng thể hệ thống giám sát tư thế ngồi (3 phân tầng chính).",
        "Hình 4.2: Sơ đồ luồng xử lý thời gian thực khép kín (One-Frame-in-Flight).",
        "Hình 6.1: Ma trận nhầm lẫn số lượng mẫu (Confusion Matrix) của mô hình SVM RBF.",
        "Hình 6.2: Ma trận nhầm lẫn chuẩn hóa theo tỷ lệ (Normalized Confusion Matrix) của mô hình SVM RBF."
    ]
    for fig in figures_list:
        add_bullet_point(doc, fig)
        
    add_styled_heading(doc, "Danh mục Bảng biểu", level=2)
    tables_list = [
        "Bảng 3.1: So sánh đa tiêu chí giữa các hướng tiếp cận nhận diện tư thế ngồi.",
        "Bảng 3.2: Tổng hợp quá trình tiến hóa và cải tiến kiến trúc qua các phiên bản V01, V02, V03.",
        "Bảng 3.3: Danh sách và ý nghĩa sinh trắc học của 6 keypoint được lựa chọn.",
        "Bảng 3.4: Bảng đặc tả chi tiết 12 đặc trưng hình học thô cơ sở (RAW12).",
        "Bảng 3.5: Bảng đặc tả chi tiết 13 đặc trưng đại diện tương đối chuẩn hóa (REP13).",
        "Bảng 3.6: So sánh đặc tính lý thuyết giữa 4 thuật toán Machine Learning khảo sát.",
        "Bảng 4.1: Danh mục và đặc tả chức năng của 8 module cốt lõi trong hệ thống.",
        "Bảng 5.1: Danh mục công nghệ, thư viện, framework và lý do lựa chọn sử dụng.",
        "Bảng 6.1: Phân bố số lượng mẫu theo các lớp tư thế trong tập dữ liệu thực nghiệm.",
        "Bảng 6.2: Bảng so sánh hiệu năng giữa 4 mô hình học máy trên không gian REP13 (Nested LOPO).",
        "Bảng 6.3: Hiệu năng phân loại chi tiết (Precision, Recall, F1) theo từng lớp của SVM RBF.",
        "Bảng 6.4: Ma trận nhầm lẫn số lượng mẫu phân loại trên 3,976 mẫu kiểm thử độc lập.",
        "Bảng 6.5: Các chỉ số hiệu năng vận hành thời gian thực đo đạc trên máy tính văn phòng.",
        "Bảng 7.1: Phân công nhiệm vụ chi tiết và sản phẩm bàn giao của từng thành viên trong nhóm.",
        "Bảng 9.1: Bảng tổng hợp vai trò và phương thức kiểm chứng công cụ AI trong quá trình thực hiện.",
        "Bảng B.1: Không gian tìm kiếm siêu tham số (Grid Search Space) của 4 thuật toán học máy.",
        "Bảng B.2: Bộ siêu tham số tối ưu chốt cho phiên bản Production của từng thuật toán.",
        "Bảng B.3: Thông số cấu hình phần cứng và môi trường thực nghiệm.",
        "Bảng D.1: Chi tiết kết quả 14 Outer LOPO Folds của mô hình SVM RBF.",
        "Bảng D.2: Bảng đối sánh Macro F1 của 14 cá nhân giữa 4 thuật toán Machine Learning."
    ]
    for tb in tables_list:
        add_bullet_point(doc, tb)

    # =========================================================================
    # CHƯƠNG 1. TỔNG QUAN BÀI TOÁN VÀ MỤC TIÊU
    # =========================================================================
    add_styled_heading(doc, "CHƯƠNG 1. TỔNG QUAN BÀI TOÁN VÀ MỤC TIÊU", level=1)
    
    add_styled_heading(doc, "1.1. Bối cảnh và lý do chọn đề tài", level=2)
    add_body_paragraph(doc, "Trong thời đại cách mạng công nghiệp 4.0, máy tính cá nhân và laptop đã trở thành công cụ lao động không thể thiếu đối với học sinh, sinh viên và nhân viên văn phòng. Tuy nhiên, thói quen ngồi làm việc tĩnh tại liên tục trong nhiều giờ liền lại kéo theo những hiểm họa khôn lường đối với sức khỏe cơ xương khớp.")
    add_body_paragraph(doc, "Các nghiên cứu y khoa về công thái học (Ergonomics) chỉ ra rằng, khi quá tập trung vào màn hình, con người có xu hướng vô thức rướn cổ về phía trước, gù lưng hoặc nghiêng vẹo sang một bên để giảm bớt sự căng thẳng của cơ bắp. Cứ mỗi 2.5 cm đầu dịch chuyển về phía trước, áp lực đè nặng lên các đốt sống cổ lại tăng thêm tương đương gần 4.5 kg. Ở trạng thái cúi 60°, sức nặng mà cột sống cổ phải chịu tải có thể lên tới 27 kg. Về lâu dài, các thói quen xấu này dẫn tới các chứng bệnh mãn tính nguy hiểm: hội chứng cổ rùa (Text Neck Syndrome), thoái hóa cột sống cổ sớm, thoát vị đĩa đệm, đau dây thần kinh tọa và cong vẹo cột sống học đường.")
    add_body_paragraph(doc, "Mặc dù người dùng đều ý thức được tác hại này, họ không thể tự kiểm soát tư thế của mình một cách liên tục nếu thiếu một công cụ hỗ trợ thông minh. Các thiết bị cảm biến đeo (wearable sensors) thường gây khó chịu, vướng víu và bất tiện khi phải sạc pin thường xuyên; trong khi các ứng dụng hẹn giờ cố định (Pomodoro) không có khả năng giám sát trực quan xem người dùng có thực sự ngồi đúng hay không. Xuất phát từ thực trạng đó, nhóm quyết định nghiên cứu và xây dựng hệ thống Smart Posture Monitor nhằm tự động phát hiện, đánh giá và nhắc nhở tư thế ngồi thời gian thực thông qua webcam máy tính.")

    add_styled_heading(doc, "1.2. Phát biểu bài toán nhận diện tư thế", level=2)
    add_body_paragraph(doc, "Bài toán đặt ra cho hệ thống là: Từ luồng video đầu vào (Input Frames) thu nhận liên tục từ webcam 2D tiêu chuẩn của máy tính, hệ thống cần tự động phát hiện người, định vị các điểm mốc giải phẫu trọng yếu trên cơ thể, trích xuất các đặc trưng hình học có ý nghĩa và phân loại chính xác trạng thái ngồi hiện tại của người dùng vào một trong bốn nhãn lớp công thái học:")
    add_bullet_point(doc, "Tư thế ngồi thẳng lưng, cổ và vai cân bằng đúng chuẩn công thái học.", "1. correct: ")
    add_bullet_point(doc, "Tư thế cúi đầu, rướn cổ hoặc gù lưng về phía màn hình máy tính.", "2. forward_slouch: ")
    add_bullet_point(doc, "Tư thế nghiêng đầu hoặc vẹo cột sống sang phía bên trái.", "3. lean_left: ")
    add_bullet_point(doc, "Tư thế nghiêng đầu hoặc vẹo cột sống sang phía bên phải.", "4. lean_right: ")
    add_body_paragraph(doc, "Đồng thời, hệ thống phải theo dõi chuỗi thời gian để kích hoạt cảnh báo thông minh (banner đỏ thị giác + chuông âm thanh) khi người dùng duy trì tư thế sai liên tục vượt quá ngưỡng thời gian cho phép (mặc định 2.0 giây), và tổng kết phiên làm việc qua Điểm số Công thái học (Ergonomics Score).")

    add_styled_heading(doc, "1.3. Mục tiêu nghiên cứu và phát triển", level=2)
    add_body_paragraph(doc, "Để giải quyết trọn vẹn bài toán trên, nhóm đặt ra ba mục tiêu nghiên cứu cốt lõi:")
    add_bullet_point(doc, "Thay vì áp dụng ngưỡng cứng nhắc cho mọi đối tượng, hệ thống phải có khả năng thích ứng linh hoạt với sự khác biệt về vóc dáng, chiều cao, chiều dài cổ và khoảng cách đặt webcam của từng cá nhân thông qua cơ chế Personal Baseline Calibration 30 mẫu, chuyển đổi từ RAW12 sang không gian đặc trưng tương đối REP13.", "Mục tiêu 1 – Độ chính xác và Cá nhân hóa cao: ")
    add_bullet_point(doc, "Khắc phục triệt để hiện tượng nhấp nháy chuyển nhãn (flickering) và triệt tiêu báo động sai khi người dùng chỉ quay đầu nói chuyện thông qua bộ lọc Yaw Gating kết hợp cửa sổ trượt Majority Vote và cơ chế trễ Hysteresis.", "Mục tiêu 2 – Tính ổn định thời gian thực: ")
    add_bullet_point(doc, "Triển khai một ứng dụng Web Dashboard hoàn chỉnh, giao diện Shadcn UI hiện đại, hỗ trợ Dark/Light mode, biểu đồ Chart.js trực quan, và bảo đảm vận hành 100% Offline trên CPU máy tính văn phòng, bảo mật tuyệt đối dữ liệu hình ảnh người dùng.", "Mục tiêu 3 – Tính ứng dụng thực tiễn và Bảo mật: ")

    add_styled_heading(doc, "1.4. Phạm vi và giới hạn của đề tài", level=2)
    add_body_paragraph(doc, "Về bài toán và dữ liệu: Hệ thống tập trung phân loại 4 trạng thái tư thế ngồi làm việc phổ biến nhất của phần thân trên dựa trên dữ liệu ảnh 2D RGB từ webcam thông thường, chưa mở rộng sang ước lượng chiều sâu 3D (Depth camera) hoặc phân tích tư thế phần thân dưới (hông, chân).")
    add_body_paragraph(doc, "Về giao thức bố trí camera: Camera được đặt cố định ở góc chếch khoảng 45° về phía bên trái của người dùng (góc quan sát tối ưu nhất để nhìn rõ đồng thời cả độ gập cổ và độ nghiêng vai). Ảnh đầu vào là ảnh gốc không lật gương (unmirrored) để đảm bảo phân định chính xác hướng nghiêng trái / phải.")
    add_body_paragraph(doc, "Về quy trình vận hành: Người dùng cần thực hiện bước hiệu chuẩn mốc chuẩn cá nhân (ngồi thẳng lưng trong khoảng 2-3 giây đầu để thu 30 mẫu correct) trước khi bước vào phiên giám sát tự động.")
    add_body_paragraph(doc, "Về mục đích ứng dụng: Sản phẩm hướng tới mục tiêu hỗ trợ cải thiện thói quen ngồi làm việc và nâng cao nhận thức bảo vệ sức khỏe, không đóng vai trò là thiết bị chẩn đoán y khoa chuyên dụng.")

    # =========================================================================
    # CHƯƠNG 2. YÊU CẦU VÀ CHỨC NĂNG HỆ THỐNG
    # =========================================================================
    add_styled_heading(doc, "CHƯƠNG 2. YÊU CẦU VÀ CHỨC NĂNG HỆ THỐNG", level=1)
    
    add_styled_heading(doc, "2.1. Yêu cầu chức năng (Functional Requirements)", level=2)
    add_body_paragraph(doc, "Hệ thống Smart Posture Monitor được phân rã thành 7 phân hệ nghiệp vụ chính, bảo đảm thực hiện đầy đủ chu trình từ thu nhận video, nhận diện AI cho đến cảnh báo và trực quan hóa dữ liệu:")
    
    add_styled_heading(doc, "2.1.1. Phân hệ thu nhận và truyền tải hình ảnh (Video & Frame Acquisition)", level=3)
    add_bullet_point(doc, "Thu nhận luồng video webcam thời gian thực trên trình duyệt thông qua API navigator.mediaDevices.getUserMedia với độ phân giải tiêu chuẩn 640x480 pixel.")
    add_bullet_point(doc, "Mã hóa khung hình liên tục tại Client thành chuỗi nhị phân Base64 và truyền tải hai chiều lên máy chủ Backend thông qua giao thức WebSocket (/ws/stream).")
    add_bullet_point(doc, "Đồng bộ thời gian truyền nhận (Latency Tracking): Gắn kèm mốc thời gian phát client_time để tính toán chính xác độ trễ trọn vòng (Round-Trip Ping) giữa trình duyệt và máy chủ.")

    add_styled_heading(doc, "2.1.2. Phân hệ thị giác máy tính và trích xuất đặc trưng (Computer Vision & Feature Engineering)", level=3)
    add_bullet_point(doc, "Định vị dáng người và trích xuất 6 điểm mốc giải phẫu cốt lõi vùng thân trên (Mũi, 2 Mắt, Tai trái, 2 Vai) bằng mô hình tích chập siêu nhẹ YOLOv8-Pose Nano.")
    add_bullet_point(doc, "Lọc chọn chủ thể trung tâm: Sử dụng hàm kết hợp vị trí trọng tâm và độ tin cậy để tự động chọn đúng người ngồi chính diện làm việc khi khung hình có nhiều người lọt vào.")
    add_bullet_point(doc, "Trích xuất vector 12 đặc trưng hình học thô (RAW12) phản ánh hướng nghiêng vai, góc nghiêng đầu, góc gập cổ và các khoảng cách không gian.")

    add_styled_heading(doc, "2.1.3. Phân hệ hiệu chuẩn tư thế cá nhân hóa (Personal Baseline Calibration)", level=3)
    add_bullet_point(doc, "Thu thập liên tục 30 khung hình hợp lệ khi người dùng ngồi đúng tư thế chuẩn (kích hoạt bằng phím tắt C hoặc nút bấm trên giao diện).")
    add_bullet_point(doc, "Xây dựng vector Baseline cá nhân: Áp dụng thuật toán Circular Median cho các đặc trưng góc và Median cho các đặc trưng khoảng cách/tỷ lệ để kháng nhiễu ngoại lai.")
    add_bullet_point(doc, "Chuyển đổi sang vector đại diện tương đối 13 chiều (REP13): Đo độ lệch tương đối so với mốc chuẩn và chuẩn hóa theo độ rộng hai vai.")

    add_styled_heading(doc, "2.1.4. Phân hệ suy luận và phân loại tư thế (Posture Classification)", level=3)
    add_bullet_point(doc, "Phân loại đa lớp trạng thái ngồi thành 4 nhãn (correct, forward_slouch, lean_left, lean_right) bằng mô hình SVM nhân RBF đã được huấn luyện tối ưu.")
    add_bullet_point(doc, "Ước lượng độ tin cậy (Probability Estimation): Trả về xác suất dự đoán của từng lớp trạng thái theo thời gian thực.")

    add_styled_heading(doc, "2.1.5. Phân hệ hậu xử lý và làm mượt thời gian (Temporal Processing)", level=3)
    add_bullet_point(doc, "Bộ lọc Yaw Gating: Đo tỷ lệ khoảng cách mắt - mũi để nhận diện hành vi quay đầu, tự động khóa trạng thái cũ nhằm chống báo động sai.")
    add_bullet_point(doc, "Cửa sổ trượt đa số (Majority Vote): Duy trì hàng đợi 7 khung hình gần nhất để bầu chọn nhãn chiếm đa số, loại bỏ hoàn toàn các khung hình dao động chớp nhoáng.")
    add_bullet_point(doc, "Độ trễ chuyển đổi trạng thái (Hysteresis): Yêu cầu tối thiểu 2 khung hình liên tiếp đồng thuận mới chính thức chuyển trạng thái hiển thị.")

    add_styled_heading(doc, "2.1.6. Phân hệ cảnh báo và thống kê phiên làm việc (Alerting & Ergonomics Statistics)", level=3)
    add_bullet_point(doc, "Cảnh báo thông minh kép: Tự động kích hoạt hiệu ứng nhấp nháy đỏ trên màn hình và phát chuông âm thanh cảnh báo khi người dùng ngồi sai liên tục vượt ngưỡng quy định (mặc định 2.0s).")
    add_bullet_point(doc, "Ghi nhận vi phạm theo đợt (Violation Episodes): Một đợt ngồi sai kéo dài chỉ tính là 1 lần vi phạm để tránh làm phiền người dùng.")
    add_bullet_point(doc, "Chấm điểm công thái học (Ergonomics Score): Tính điểm sức khỏe phiên ngồi trên thang điểm 100 theo thời gian thực dựa trên tỷ lệ thời gian ngồi đúng trừ đi trọng số các lần vi phạm.")

    add_styled_heading(doc, "2.1.7. Phân hệ bảng điều khiển và trực quan hóa (Dashboard UI)", level=3)
    add_bullet_point(doc, "Khung video webcam trực tiếp kèm lớp phủ vẽ khung xương 6 điểm (Skeleton Overlay) có thể bật/tắt linh hoạt.")
    add_bullet_point(doc, "Ma trận thẻ chỉ số KPI: Hiển thị trạng thái tư thế, Điểm công thái học, Đồng hồ thời gian phiên và Bộ đếm cảnh báo vi phạm.")
    add_bullet_point(doc, "Chế độ xem phân tích (Analytics View): Tích hợp thư viện Chart.js vẽ biểu đồ tròn phân bố thời gian các tư thế và danh sách chi tiết các đợt vi phạm.")
    add_bullet_point(doc, "Quản lý lịch sử phiên (History View): Lưu trữ phiên làm việc vào localStorage và hỗ trợ xuất dữ liệu báo cáo ra file CSV/Excel.")

    add_styled_heading(doc, "2.2. Yêu cầu phi chức năng (Non-Functional Requirements)", level=2)
    add_body_paragraph(doc, "Để có thể vận hành ổn định và mang lại trải nghiệm người dùng tối ưu trong môi trường văn phòng thực tế, hệ thống đáp ứng nghiêm ngặt các tiêu chuẩn phi chức năng sau:")
    
    table_nfr_data = [
        ["Nhóm yêu cầu", "Tiêu chuẩn kỹ thuật đặt ra", "Giải thích ý nghĩa và Giải pháp kỹ thuật trong dự án"],
        ["Tính thời gian thực (Real-time)", "Tốc độ xử lý: 15 – 22 FPS\nTổng độ trễ: < 80 ms", "Toàn bộ pipeline AI xử lý mượt mà trên CPU máy tính văn phòng thông thường, phản hồi kết quả tức thì lên giao diện web."],
        ["Độ ổn định chuỗi thời gian (Temporal Stability)", "Kháng nhiễu khung hình, triệt tiêu rung giật nhãn", "Loại bỏ hoàn toàn hiện tượng nhấp nháy nhãn (flickering) thông qua bộ lọc Yaw Gating và cơ chế kép Majority Vote + Hysteresis."],
        ["Tính dễ sử dụng & Tiếp cận (Usability)", "Không cần thiết bị chuyên dụng, giao diện thân thiện", "Chỉ yêu cầu webcam laptop sẵn có và trình duyệt web. Hỗ trợ đầy đủ phím tắt nhanh (C hiệu chuẩn, R đặt lại, Q dừng)."],
        ["Kiến trúc module hóa (Modularity)", "Tuân thủ chặt chẽ nguyên lý Single Responsibility", "Các khối PoseDetector, FeatureExtractor, Calibration, Predictor, Monitor độc lập, có thể dễ dàng bảo trì và viết Unit Test."],
        ["Hoạt động Ngoại tuyến & Bảo mật (Offline & Privacy)", "Xử lý cục bộ 100% trên thiết bị người dùng", "Không lưu trữ hay truyền tải bất kỳ hình ảnh nhạy cảm nào của người dùng lên đám mây, bảo đảm quyền riêng tư tuyệt đối."],
        ["Độ chính xác & Khái quát hóa (Generalization)", "Macro F1-score: > 0.90 trên người dùng chưa từng thấy", "Mô hình đạt Macro F1 trung bình 0.9199 qua kiểm thử nghiêm ngặt Nested Leave-One-Person-Out CV trên 14 người dùng độc lập."]
    ]
    create_table_from_data(doc, table_nfr_data, col_widths=[1.5, 1.8, 3.1], align_center_cols=[0])

    add_styled_heading(doc, "2.3. Quy trình người dùng (User Flow)", level=2)
    add_body_paragraph(doc, "Quy trình tương tác giữa người dùng và hệ thống được thiết kế tối giản, khoa học và hoàn toàn tự nhiên qua 7 bước tuần tự:")
    add_bullet_point(doc, "Người dùng mở trình duyệt truy cập Web Dashboard, nhấn 'Bật Webcam Ngay'. Hệ thống thiết lập kết nối WebSocket và hiển thị video kèm thông số FPS/Ping.", "Bước 1 - Khởi động phiên: ")
    add_bullet_point(doc, "Người dùng ngồi thẳng lưng đúng chuẩn công thái học và bấm phím tắt C. Hệ thống tự động thu 30 khung hình hợp lệ để xác lập vector mốc chuẩn Baseline riêng.", "Bước 2 - Hiệu chuẩn Baseline: ")
    add_bullet_point(doc, "Người dùng quay trở lại làm việc bình thường. Hệ thống chạy nền âm thầm phân tích tư thế từng khung hình.", "Bước 3 - Theo dõi liên tục: ")
    add_bullet_point(doc, "Pipeline AI liên tục tính toán độ lệch góc, đưa qua bộ lọc làm mượt và cập nhật trạng thái tư thế lên giao diện với tần số ~15-22 FPS.", "Bước 4 - Nhận diện AI thời gian thực: ")
    add_bullet_point(doc, "Nếu phát hiện người dùng ngồi sai (gù lưng hoặc nghiêng người) liên tục quá 2 giây, hệ thống lập tức nhấp nháy banner đỏ và phát âm thanh Bip nhắc nhở.", "Bước 5 - Cảnh báo thông minh: ")
    add_bullet_point(doc, "Kết thúc ca làm việc, người dùng nhấn 'Kết thúc phiên' (hoặc phím tắt Q/Esc). Dữ liệu phiên được tổng hợp và tự động lưu vào bộ nhớ trình duyệt.", "Bước 6 - Đóng gói phiên: ")
    add_bullet_point(doc, "Người dùng chuyển sang tab Phân tích & Lịch sử để xem biểu đồ tròn tỷ lệ tư thế, Điểm công thái học tổng kết và các đợt vi phạm để tự điều chỉnh thói quen.", "Bước 7 - Xem thống kê chi tiết: ")

    # =========================================================================
    # CHƯƠNG 3. PHÂN TÍCH VÀ LỰA CHỌN GIẢI PHÁP
    # =========================================================================
    add_styled_heading(doc, "CHƯƠNG 3. PHÂN TÍCH VÀ LỰA CHỌN GIẢI PHÁP", level=1)
    
    add_styled_heading(doc, "3.1. Phân tích các hướng tiếp cận công nghệ", level=2)
    add_body_paragraph(doc, "Trong lĩnh vực thị giác máy tính, bài toán nhận diện tư thế người ngồi có thể được tiếp cận qua ba hướng chính: (1) Phương pháp dựa trên quy tắc hình học cứng (Rule-based); (2) Phương pháp học sâu phân loại trực tiếp từ ảnh pixel (End-to-End Deep Learning); và (3) Phương pháp kết hợp Ước lượng tư thế (Pose Estimation) với Kỹ thuật đặc trưng (Feature Engineering) và Học máy cổ điển (Machine Learning).")
    
    add_caption(doc, "Bảng 3.1: So sánh đa tiêu chí giữa các hướng tiếp cận nhận diện tư thế ngồi.", is_table=True)
    create_table_from_data(doc, TABLE_COMPARISON_APPROACHES, col_widths=[1.5, 1.5, 1.6, 1.8], align_center_cols=[0])
    add_body_paragraph(doc, "Qua bảng so sánh trên, nhóm quyết định lựa chọn hướng tiếp cận thứ 3: Kết hợp Pose Estimation + Feature Engineering + Machine Learning làm nền tảng phát triển đề tài. Hướng đi này giúp tận dụng tối đa sức mạnh của mô hình Pose Estimation đã được tiền huấn luyện trên hàng triệu hình ảnh, đồng thời đưa dữ liệu về dạng các đặc trưng hình học tường minh, cho phép áp dụng cơ chế hiệu chuẩn cá nhân hóa và vận hành siêu nhẹ trên CPU thông thường.")

    add_styled_heading(doc, "3.2. Kiến trúc giải pháp tổng thể đề xuất", level=2)
    add_body_paragraph(doc, "Kiến trúc giải pháp hoàn thiện của hệ thống Smart Posture Monitor V03 là một chuỗi xử lý khép kín, phân tách rõ ràng trách nhiệm giữa các tầng nghiệp vụ:")
    
    add_image_safely(doc, "docs/extracted_media/image5.png", "Hình 3.1: Sơ đồ kiến trúc xử lý nhận diện tư thế ngồi đề xuất (Pipeline V03).", width_inches=6.0)
    
    add_body_paragraph(doc, "Hệ thống vận hành theo hai chu trình độc lập:")
    add_body_paragraph(doc, "Chu trình xây dựng mô hình (Offline Training): Dữ liệu ảnh thô được trích xuất đặc trưng RAW12, loại bỏ các khung hình hiệu chuẩn, tính toán mốc Baseline riêng cho từng phiên ghi hình, biến đổi thành REP13 và đưa vào quy trình đánh giá nghiêm ngặt Nested Leave-One-Person-Out CV để chọn ra mô hình tối ưu nhất (SVM RBF).", bold_prefix="a) ")
    add_body_paragraph(doc, "Chu trình giám sát thời gian thực (Real-time Inference): Người dùng thực hiện hiệu chuẩn mốc chuẩn trong 2-3 giây đầu. Các khung hình tiếp theo được trích xuất RAW12, trừ mốc Baseline để tạo REP13, đưa qua mô hình SVM dự đoán và lọc qua bộ lọc chuỗi thời gian trước khi hiển thị lên Web Dashboard.", bold_prefix="b) ")

    add_styled_heading(doc, "Quá trình phát triển và cải tiến qua các phiên bản (V01, V02, V03)", level=3)
    add_body_paragraph(doc, "Để đạt được kiến trúc tối ưu hiện tại, nhóm đã trải qua quá trình nghiên cứu và thực nghiệm qua ba giai đoạn tiến hóa rõ rệt:")
    
    add_caption(doc, "Bảng 3.2: Tổng hợp quá trình tiến hóa và cải tiến kiến trúc qua các phiên bản V01, V02, V03.", is_table=True)
    create_table_from_data(doc, TABLE_VERSION_EVOLUTION, col_widths=[1.5, 1.5, 1.5, 1.9], align_center_cols=[0])
    
    add_callout_box(doc, "Điểm đột phá mang tính quyết định của Phiên bản V03:",
                    "Khác biệt căn bản giữa V03 và các phiên bản trước là sự ra đời của cơ chế Personal Calibration. Thay vì cố gắng tìm kiếm một đường biên quyết định toàn cục trên các tọa độ hình học tuyệt đối (vốn luôn bị biến dạng bởi chiều cao, độ rộng vai và cự ly ngồi của từng người), V03 chuyển đổi toàn bộ bài toán sang không gian độ lệch tương đối (Relative Space) so với chính tư thế chuẩn của người đó. Nhờ vậy, độ phân tán dữ liệu giữa các cá nhân giảm mạnh 33.8%, nâng Macro F1 trên người dùng mới từ 0.846 lên 0.9199.")

    add_styled_heading(doc, "3.3. Ước lượng tư thế và lựa chọn điểm mốc cơ thể (Keypoints)", level=2)
    add_body_paragraph(doc, "Nhóm sử dụng mô hình YOLOv8-Pose (phiên bản yolo26n-pose.pt siêu nhẹ ~6MB) để phát hiện người và ước lượng vị trí các điểm mốc cơ thể. Mô hình gốc cung cấp 17 điểm mốc theo chuẩn COCO:")
    
    add_image_safely(doc, "docs/extracted_media/image4.png", "Hình 3.2: Minh họa 17 điểm mốc cơ thể theo định dạng COCO của YOLO-Pose.", width_inches=4.8)
    
    add_body_paragraph(doc, "Tuy nhiên, trong bối cảnh người dùng ngồi làm việc trước máy tính với camera đặt chếch 45° bên trái, phần thân dưới hoàn toàn bị che khuất bởi mặt bàn. Đồng thời, tai phải thường xuyên bị che khuất bởi đầu khi nhìn thẳng hoặc quay nhẹ. Do đó, việc giữ lại toàn bộ 17 điểm mốc sẽ gây lãng phí tài nguyên và làm tăng nguy cơ nhiễu dữ liệu. Nhóm quyết định tinh gọn lại đúng 6 điểm mốc cốt lõi thuộc vùng thân trên:")
    
    add_caption(doc, "Bảng 3.3: Danh sách và ý nghĩa sinh trắc học của 6 keypoint được lựa chọn.", is_table=True)
    create_table_from_data(doc, TABLE_KEYPOINTS, col_widths=[0.6, 1.5, 0.9, 1.2, 2.2], align_center_cols=[0, 2])

    add_styled_heading(doc, "Thuật toán chọn lọc chủ thể trung tâm tối ưu", level=3)
    add_body_paragraph(doc, "Trong môi trường làm việc thực tế, khung hình camera có thể xuất hiện đồng nghiệp đi ngang qua phía sau hoặc người ngồi bên cạnh. Để luôn khóa đúng người sử dụng chính, module PoseDetector tính toán điểm ưu tiên Si cho từng người i phát hiện được theo công thức:")
    add_body_paragraph(doc, "S_i = 0.7 · C_i + 0.3 · P_i", bold_prefix="Công thức điểm ưu tiên chủ thể: ")
    add_body_paragraph(doc, "Trong đó: C_i là chỉ số đo mức độ gần tâm hình ảnh (centrality, dao động từ 0 đến 1), và P_i là độ tin cậy phát hiện người do YOLO cung cấp. Trọng số 0.7 ưu tiên rất cao cho đối tượng ngồi chính diện camera.")

    add_styled_heading(doc, "Kiểm tra và chuẩn hóa dữ liệu Keypoint", level=3)
    add_body_paragraph(doc, "Để ngăn chặn các khung hình suy biến làm sai lệch mô hình, module FeatureExtractor áp dụng bộ lọc chất lượng nghiêm ngặt: (1) Đủ 6 điểm keypoint; (2) Độ tự tin của từng keypoint phải đạt ngưỡng tối thiểu c_i ≥ 0.35; (3) Tọa độ không chứa giá trị NaN hoặc vô cực; (4) Khoảng cách hai mắt và khoảng cách hai vai phải lớn hơn ngưỡng tối thiểu để tránh lỗi chia cho 0.")

    add_styled_heading(doc, "3.4. Kỹ thuật thiết kế đặc trưng hình học (RAW12)", level=2)
    add_body_paragraph(doc, "Từ tọa độ 6 điểm mốc giải phẫu hợp lệ, hệ thống tính toán 12 đặc trưng hình học thô (RAW12) phản ánh toàn diện các biến dạng của phần thân trên theo 4 nhóm chuyên biệt:")
    
    add_caption(doc, "Bảng 3.4: Bảng đặc tả chi tiết 12 đặc trưng hình học thô cơ sở (RAW12).", is_table=True)
    create_table_from_data(doc, TABLE_RAW12_SPEC, col_widths=[0.8, 1.8, 1.2, 1.4, 0.6, 1.6], align_center_cols=[0, 4])

    add_styled_heading(doc, "Nguyên lý tính toán hình học", level=3)
    add_body_paragraph(doc, "Các góc nghiêng được tính toán thông qua hàm lượng giác atan2 có dấu để bảo toàn trọn vẹn hướng nghiêng: θ = atan2(Δy, Δx) * 180 / π. Độ chênh lệch giữa hai góc luôn được đưa qua hàm chuẩn hóa wrap để bảo đảm giá trị luôn nằm trong chu kỳ tuần hoàn [-180°, 180°), triệt tiêu hoàn toàn sai số khi góc dao động qua đường ranh giới.")

    add_styled_heading(doc, "3.5. Hiệu chuẩn cá nhân hóa và Biểu diễn đặc trưng tương đối (REP13)", level=2)
    add_body_paragraph(doc, "Quy trình chuyển đổi từ RAW12 sang REP13 được minh họa qua sơ đồ kiến trúc sau:")
    
    add_image_safely(doc, "docs/extracted_media/image3.png", "Hình 3.3: Quy trình hiệu chuẩn Baseline cá nhân hóa và biến đổi RAW12 sang REP13.", width_inches=5.6)
    
    add_body_paragraph(doc, "Thuật toán Circular Median cho đặc trưng góc: Với các đại lượng góc tuần hoàn (RAW01 đến RAW04), phép tính trung vị thông thường sẽ cho kết quả sai lệch nghiêm trọng nếu các góc nằm sát ranh giới ±180° (ví dụ trung vị của -179° và +179° sẽ thành 0°, trong khi góc đại diện thực tế phải là 180°). Hệ thống giải quyết bằng cách tìm mẫu góc có tổng khoảng cách góc tới các mẫu khác nhỏ nhất làm mốc tham chiếu, sau đó mở rộng đường tròn và tính trung vị tuyến tính.")
    add_body_paragraph(doc, "Chuẩn hóa độ rộng vai tham chiếu W_0: Mọi khoảng cách không gian (tâm mắt, tâm vai, độ lệch ngang/dọc) đều được chia cho W_0 (chiều rộng hai vai trong Baseline), chuyển các đại lượng pixel thành giá trị không thứ nguyên (dimensionless). Nhờ đó, người dùng ngồi gần hay ngồi xa camera đều cho ra các vector đặc trưng tương đồng.")
    
    add_caption(doc, "Bảng 3.5: Bảng đặc tả chi tiết 13 đặc trưng đại diện tương đối chuẩn hóa (REP13).", is_table=True)
    create_table_from_data(doc, TABLE_REP13_SPEC, col_widths=[0.8, 2.0, 0.9, 1.5, 0.8, 1.4], align_center_cols=[0, 2])

    add_styled_heading(doc, "3.6. Nghiên cứu và lựa chọn mô hình Machine Learning", level=2)
    add_body_paragraph(doc, "Sau khi chuyển đổi sang không gian REP13, bài toán trở thành phân loại dữ liệu dạng bảng (Tabular Data) với số chiều thấp (13 chiều) và 4 lớp nhãn. Nhóm tiến hành khảo sát và đối sánh 4 thuật toán học máy phổ biến:")
    
    add_caption(doc, "Bảng 3.6: So sánh đặc tính lý thuyết giữa 4 thuật toán Machine Learning khảo sát.", is_table=True)
    create_table_from_data(doc, TABLE_MODEL_ALGORITHMS, col_widths=[1.4, 1.5, 1.5, 1.5, 1.5], align_center_cols=[0])

    add_styled_heading(doc, "3.7. Bộ lọc chuỗi thời gian (Temporal Monitoring & Yaw Gating)", level=2)
    add_body_paragraph(doc, "Một vấn đề kinh điển trong thị giác máy tính là hiện tượng rung giật nhãn (flickering): Do nhiễu ánh sáng hoặc cử động thở nhẹ, mô hình có thể dự đoán sai lệch trong 1-2 khung hình đơn lẻ. Nếu hiển thị trực tiếp lên giao diện, người dùng sẽ thấy nhãn nhảy liên tục, gây khó chịu và kích hoạt chuông cảnh báo sai.")
    add_body_paragraph(doc, "Để khắc phục triệt để vấn đề này, module TemporalMonitor được tích hợp 3 cơ chế lọc nối tiếp:")
    add_bullet_point(doc, "Đo tỷ lệ bề rộng mắt - mũi R = d(Left Eye, Nose) / d(Right Eye, Nose). Khi người dùng quay đầu sang hai bên, tỷ lệ này sẽ rơi ra ngoài khoảng an toàn [0.45, 1.80]. Hệ thống tự động kích hoạt chế độ Conservative Yaw Mode: Khóa cố định trạng thái thân trên ổn định trước đó và không đưa dự đoán của khung hình bị quay mặt vào cửa sổ biểu quyết.", "1. Bộ lọc quay mặt (Yaw Gating): ")
    add_bullet_point(doc, "Duy trì hàng đợi 7 khung hình gần nhất. Nhãn chiếm đa số tuyệt đối trong cửa sổ được chọn làm nhãn ứng viên, loại bỏ hoàn toàn các khung hình dao động lẻ tẻ.", "2. Cửa sổ trượt đa số (Majority Vote W=7): ")
    add_bullet_point(doc, "Yêu cầu nhãn ứng viên mới phải duy trì liên tiếp tối thiểu 2 khung hình trước khi chính thức chuyển đổi trạng thái hiển thị.", "3. Cơ chế trễ trạng thái (Hysteresis): ")

    # =========================================================================
    # CHƯƠNG 4. THIẾT KẾ CHƯƠNG TRÌNH VÀ HỆ THỐNG
    # =========================================================================
    add_styled_heading(doc, "CHƯƠNG 4. THIẾT KẾ CHƯƠNG TRÌNH VÀ HỆ THỐNG", level=1)
    
    add_styled_heading(doc, "4.1. Kiến trúc phân tầng của hệ thống", level=2)
    add_body_paragraph(doc, "Hệ thống Smart Posture Monitor được thiết kế theo kiến trúc 3 khối chức năng phân tầng rõ rệt:")
    
    add_image_safely(doc, "docs/extracted_media/image6.png", "Hình 4.1: Sơ đồ kiến trúc tổng thể hệ thống giám sát tư thế ngồi (3 phân tầng chính).", width_inches=5.8)
    
    add_body_paragraph(doc, "Khối 1 – Thu nhận dữ liệu: Tiếp nhận luồng video từ webcam, giải mã khung hình và đưa qua YOLO-Pose để phát hiện 6 điểm mốc giải phẫu.", bold_prefix="• ")
    add_body_paragraph(doc, "Khối 2 – Xử lý và Nhận diện: Trích xuất đặc trưng RAW12, trừ vector Baseline cá nhân để tạo REP13 và đưa vào mô hình SVM RBF để phân loại đa lớp.", bold_prefix="• ")
    add_body_paragraph(doc, "Khối 3 – Giám sát và Hiển thị: Ổn định chuỗi thời gian qua TemporalMonitor, tính toán thống kê phiên qua SessionStatistics và truyền dữ liệu JSON qua WebSocket để render lên Dashboard.", bold_prefix="• ")

    add_styled_heading(doc, "4.2. Thiết kế chi tiết các module nghiệp vụ", level=2)
    add_caption(doc, "Bảng 4.1: Danh mục và đặc tả chức năng của 8 module cốt lõi trong hệ thống.", is_table=True)
    create_table_from_data(doc, TABLE_MODULES, col_widths=[1.5, 1.5, 2.0, 1.2, 1.2], align_center_cols=[0])

    add_styled_heading(doc, "4.3. Thiết kế luồng xử lý thời gian thực (One-Frame-in-Flight)", level=2)
    add_image_safely(doc, "docs/extracted_media/image7.png", "Hình 4.2: Sơ đồ luồng xử lý thời gian thực khép kín (One-Frame-in-Flight).", width_inches=4.2)
    
    add_callout_box(doc, "Giải pháp kỹ thuật đột phá: Cơ chế One-Frame-in-Flight / Latest-Frame-Wins",
                    "Trong các hệ thống truyền nhận video qua WebSocket thông thường, nếu Client đẩy ảnh theo chu kỳ cố định (ví dụ setInterval 50ms) trong khi Server xử lý mất 60ms, các khung hình sẽ bị dồn ứ trong hàng đợi (Backlog Queuing), khiến độ trễ hiển thị tăng dần lên hàng chục giây. Nhóm đã giải quyết triệt để vấn đề này bằng cơ chế điều khiển luồng bất đồng bộ: Frontend chỉ chụp và gửi khung hình tiếp theo khi khung hình trước đã nhận được phản hồi từ Server (cờ frameInFlight = false). Đồng thời tách riêng Canvas hiển thị và Offscreen Canvas chụp ảnh, bảo đảm độ trễ luôn ổn định dưới 50ms.")

    add_styled_heading(doc, "4.4. Quy trình huấn luyện và kiểm thử mô hình", level=2)
    add_body_paragraph(doc, "Quy trình huấn luyện tuân thủ nghiêm ngặt nguyên tắc ngăn chặn rò rỉ dữ liệu (Data Leakage Prevention): Toàn bộ 480 khung hình dùng để tính Baseline (30 khung hình correct đầu tiên của mỗi phiên ghi hình) được tách riêng và loại bỏ hoàn toàn khỏi tập huấn luyện cũng như tập kiểm thử.")
    add_body_paragraph(doc, "Mô hình được đánh giá thông qua giao thức lồng nhau Nested Leave-One-Person-Out CV (14 folds ngoài tương ứng 14 cá nhân; trong mỗi fold ngoài, dùng StratifiedGroupKFold 4 folds trên 13 người còn lại để tìm kiếm siêu tham số tối ưu).")

    add_styled_heading(doc, "4.5. Thiết kế giao diện người dùng (Dashboard UI)", level=2)
    add_body_paragraph(doc, "Giao diện Web Dashboard được xây dựng theo ngôn ngữ thiết kế Shadcn UI hiện đại trên nền tảng TailwindCSS, hỗ trợ cả 2 giao diện Sáng (Light Mode) và Tối (Dark Mode), bố cục khoa học gồm 3 phân vùng chính:")
    add_bullet_point(doc, "Logo nhận diện thương hiệu, các nút chuyển đổi màn hình (Tổng quan, Phân tích & Biểu đồ, Lịch sử phiên) và nhãn hiển thị phiên bản hệ thống.", "1. Thanh điều hướng bên trái (Navigation Sidebar): ")
    add_bullet_point(doc, "Tiêu đề trang, đèn hiệu báo trạng thái kết nối WebSocket, nút Cài đặt ngưỡng cảnh báo (1-60s), nút bật/tắt âm thanh chuông báo, nút chuyển Dark/Light mode và nút Kết thúc phiên làm việc.", "2. Thanh công cụ đầu trang (Header Bar): ")
    add_bullet_point(doc, "Bố cục lưới chia đôi: Cột trái (8/12) trình chiếu video webcam kèm lớp vẽ khung xương 6 điểm (Canvas Overlay), huy hiệu FPS/Ping và banner đỏ nhấp nháy khi vi phạm; Cột phải (4/12) gồm 4 thẻ KPI chỉ số, thước đo góc nghiêng sinh trắc học và hộp thoại gợi ý lời khuyên công thái học.", "3. Khu vực giám sát trung tâm (Dashboard Grid): ")

    # =========================================================================
    # CHƯƠNG 5. THƯ VIỆN, FRAMEWORK VÀ CÔNG NGHỆ
    # =========================================================================
    add_styled_heading(doc, "CHƯƠNG 5. THƯ VIỆN, FRAMEWORK VÀ CÔNG NGHỆ", level=1)
    add_body_paragraph(doc, "Để hiện thực hóa giải pháp từ khâu nghiên cứu thuật toán AI đến triển khai một ứng dụng web hoàn chỉnh, nhóm đã chọn lọc và tích hợp các công nghệ tối ưu nhất trong hệ sinh thái Python và Web hiện đại:")
    
    add_caption(doc, "Bảng 5.1: Danh mục công nghệ, thư viện, framework và lý do lựa chọn sử dụng.", is_table=True)
    create_table_from_data(doc, TABLE_TECH_STACK, col_widths=[1.5, 0.9, 1.8, 2.2], align_center_cols=[0, 1])

    # =========================================================================
    # CHƯƠNG 6. THỰC NGHIỆM, KẾT QUẢ VÀ MINH HỌA SẢN PHẨM
    # =========================================================================
    add_styled_heading(doc, "CHƯƠNG 6. THỰC NGHIỆM, KẾT QUẢ VÀ MINH HỌA SẢN PHẨM", level=1)
    
    add_styled_heading(doc, "6.1. Thu thập và Phân tích tập dữ liệu thực nghiệm (Dataset & EDA)", level=2)
    add_body_paragraph(doc, "Tập dữ liệu V03 được nhóm tự thu thập từ 14 tình nguyện viên (person01 đến person14) đa dạng về vóc dáng, giới tính, chiều cao và trang phục, thực hiện qua 16 phiên ghi hình (recordings). Toàn bộ ảnh được thu ở độ phân giải 640x480, góc chếch 45° bên trái, không lật gương.")
    add_body_paragraph(doc, "Tổng số ảnh thu thập ban đầu: 4,814 ảnh; Số mẫu hợp lệ đạt ngưỡng: 4,456 mẫu; Số mẫu bị loại (rejected): 358 mẫu (tỷ lệ 7.44%, đều do đối tượng cúi quá sát màn hình khiến độ tin cậy keypoint < 0.35).")
    
    add_caption(doc, "Bảng 6.1: Phân bố số lượng mẫu theo các lớp tư thế trong tập dữ liệu thực nghiệm.", is_table=True)
    create_table_from_data(doc, TABLE_DATASET_DISTRIBUTION, col_widths=[1.3, 2.2, 1.0, 1.1, 1.1, 0.7], align_center_cols=[0, 2, 3, 4, 5])

    add_body_paragraph(doc, "Kết quả phân tích thăm dò dữ liệu (EDA): Độ phân tán chuẩn hóa trung vị của dữ liệu thô RAW12 giữa 14 người dùng là 0.6321, nhưng sau khi chuẩn hóa qua Personal Baseline trong không gian REP13, độ phân tán này giảm mạnh xuống chỉ còn 0.4185 (giảm 33.8%). Điều này chứng minh không gian REP13 đã triệt tiêu hiệu quả sự sai khác về thể hình và khoảng cách ngồi.")

    add_styled_heading(doc, "6.2. Phương pháp đánh giá mô hình (Nested LOPO CV)", level=2)
    add_body_paragraph(doc, "Để đảm bảo tính khách quan tuyệt đối và chống rò rỉ chủ thể (Subject Leakage), nhóm áp dụng giao thức Nested Leave-One-Person-Out CV với 14 folds ngoài (mỗi fold giữ lại toàn bộ dữ liệu của 1 người làm tập kiểm thử) và 4 folds trong (StratifiedGroupKFold trên 13 người còn lại để tìm kiếm siêu tham số tối ưu).")

    add_styled_heading(doc, "6.3. Đánh giá và so sánh hiệu năng các mô hình Machine Learning", level=2)
    add_caption(doc, "Bảng 6.2: Bảng so sánh hiệu năng giữa 4 mô hình học máy trên không gian REP13 (Nested LOPO).", is_table=True)
    create_table_from_data(doc, TABLE_MODEL_COMPARISON, col_widths=[0.6, 1.8, 1.3, 1.0, 1.0, 1.0, 1.0, 1.1], align_center_cols=[0, 2, 3, 4, 5, 6, 7])
    
    add_body_paragraph(doc, "Mô hình SVM nhân RBF giành chiến thắng toàn diện với Macro F1 trung bình đạt 0.9199 và Accuracy đạt 0.9329. Đặc biệt, SVM có độ lệch chuẩn nhỏ nhất (Std = 0.1100) và hiệu năng ở tình huống xấu nhất cao nhất (Worst Person F1 = 0.6719). Các mô hình dạng cây (RF, XGBoost) gặp khó khăn do các lát cắt trực giao không khớp tốt với đường biên mặt cầu của vector góc.")

    add_styled_heading(doc, "Hiệu năng chi tiết theo từng lớp của mô hình SVM RBF", level=3)
    add_caption(doc, "Bảng 6.3: Hiệu năng phân loại chi tiết (Precision, Recall, F1) theo từng lớp của SVM RBF.", is_table=True)
    create_table_from_data(doc, TABLE_PER_CLASS_PERFORMANCE, col_widths=[2.4, 1.2, 1.2, 1.2, 1.4], align_center_cols=[1, 2, 3, 4])

    add_styled_heading(doc, "Phân tích ma trận nhầm lẫn (Confusion Matrix Analysis)", level=3)
    add_caption(doc, "Bảng 6.4: Ma trận nhầm lẫn số lượng mẫu phân loại trên 3,976 mẫu kiểm thử độc lập.", is_table=True)
    create_table_from_data(doc, TABLE_CONFUSION_MATRIX, col_widths=[1.8, 1.1, 1.3, 1.1, 1.1, 1.0], align_center_cols=[1, 2, 3, 4, 5])

    # Thêm ảnh Confusion Matrix thực tế từ thư mục results
    add_image_safely(doc, "results/v03_lopo/confusion_matrix_svm_rbf.png", "Hình 6.1: Ma trận nhầm lẫn số lượng mẫu (Confusion Matrix) của mô hình SVM RBF.", width_inches=5.2)
    add_image_safely(doc, "results/v03_lopo/confusion_matrix_normalized_svm_rbf.png", "Hình 6.2: Ma trận nhầm lẫn chuẩn hóa theo tỷ lệ (Normalized Confusion Matrix) của mô hình SVM RBF.", width_inches=5.2)

    add_body_paragraph(doc, "Phân tích nguyên nhân sai số: Cặp nhầm lẫn lớn nhất là giữa lean_right và forward_slouch (69 mẫu). Nguyên nhân hoàn toàn xuất phát từ nguyên lý phối cảnh hình học (Perspective Foreshortening): Khi camera đặt chếch 45° bên trái, hành vi nghiêng người sang bên phải sẽ khiến cơ thể dịch chuyển xa dần ống kính, làm thu hẹp khoảng cách hai vai và hạ thấp tọa độ mắt tương tự như khi rướn cúi về phía trước. Ngược lại, khả năng phân biệt giữa lean_left và lean_right đạt độ chính xác gần như tuyệt đối (chỉ có 2/1028 mẫu nhầm lẫn).")

    add_styled_heading(doc, "6.4. Đánh giá hiệu năng vận hành thời gian thực", level=2)
    add_caption(doc, "Bảng 6.5: Các chỉ số hiệu năng vận hành thời gian thực đo đạc trên máy tính văn phòng.", is_table=True)
    create_table_from_data(doc, TABLE_REALTIME_METRICS, col_widths=[2.4, 1.6, 1.4, 2.0], align_center_cols=[1, 2])

    add_styled_heading(doc, "6.5. Đánh giá hiệu quả của bộ lọc Temporal Monitoring", level=2)
    add_body_paragraph(doc, "Hiệu quả khử nhiễu quay đầu (Yaw Gating): Khi người dùng quay mặt sang trái/phải để nói chuyện, tỷ lệ khoảng cách mắt-mũi biến động vượt ngưỡng [0.45, 1.80]. Chế độ Conservative Yaw Mode đã loại bỏ 100% các cảnh báo sai do cử động quay đầu gây ra.")
    add_body_paragraph(doc, "Hiệu quả chống nhấp nháy nhãn (Flickering): Cửa sổ trượt Majority Vote (W=7) kết hợp cơ chế trễ Hysteresis (2 khung hình) đã giảm tới 96.4% hiện tượng nhảy nhãn chớp nhoáng khi người dùng chuyển thế ngồi từ từ, tạo trải nghiệm mượt mà, tin cậy trên giao diện.")

    add_styled_heading(doc, "6.6. Đánh giá cơ chế thống kê và Điểm Công thái học", level=2)
    add_body_paragraph(doc, "Công thức tính Điểm Công thái học (Ergonomics Score) theo thời gian thực:")
    add_body_paragraph(doc, "Ergonomics Score = max(0, min(100, (T_correct / T_total) * 100 - (N_violations * 2)))", bold_prefix="Công thức: ")
    add_body_paragraph(doc, "Mỗi đợt ngồi sai kéo dài liên tục được gom thành 01 đợt vi phạm (Violation Episode), trừ 2 điểm trên tổng điểm 100, giúp kích thích người dùng chủ động sửa sai ngay khi nghe chuông báo mà không làm tăng vọt số lượng vi phạm.")

    add_styled_heading(doc, "6.7. Tổng kết đánh giá ưu điểm và hạn chế của hệ thống", level=2)
    add_body_paragraph(doc, "Ưu điểm vượt trội: Cá nhân hóa linh hoạt qua 30 mẫu Baseline; độ chính xác cao (Macro F1 0.9199); vận hành siêu nhẹ (15-22 FPS trên CPU); bảo vệ quyền riêng tư 100% offline; giao diện Web Dashboard trực quan, hiện đại.")
    add_body_paragraph(doc, "Hạn chế còn tồn tại: Bắt buộc người dùng phải ngồi chuẩn trong 2-3 giây đầu để hiệu chuẩn Baseline; hệ thống tối ưu nhất ở góc đặt camera 45° bên trái (sẽ bị giảm độ chính xác nếu đặt camera trực diện hoặc sau lưng).")

    # =========================================================================
    # CHƯƠNG 7. PHÂN CHIA CÔNG VIỆC TRONG NHÓM
    # =========================================================================
    add_styled_heading(doc, "CHƯƠNG 7. PHÂN CHIA CÔNG VIỆC TRONG NHÓM", level=1)
    add_body_paragraph(doc, "Đề tài được thực hiện bởi nhóm gồm 3 thành viên, phân công nhiệm vụ cụ thể dựa trên sở trường chuyên môn của từng thành viên:")
    
    add_caption(doc, "Bảng 7.1: Phân công nhiệm vụ chi tiết và sản phẩm bàn giao của từng thành viên trong nhóm.", is_table=True)
    create_table_from_data(doc, TABLE_TASK_ASSIGNMENT, col_widths=[1.5, 1.4, 2.4, 2.1], align_center_cols=[0])

    # =========================================================================
    # CHƯƠNG 8. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN
    # =========================================================================
    add_styled_heading(doc, "CHƯƠNG 8. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN", level=1)
    
    add_styled_heading(doc, "8.1. Các kết quả chính đạt được", level=2)
    add_body_paragraph(doc, "Sau thời gian nghiêm túc nghiên cứu và triển khai, nhóm đã hoàn thành toàn diện các mục tiêu đề ra:")
    add_bullet_point(doc, "Xây dựng thành công tập dữ liệu 4,456 mẫu hợp lệ trên 14 cá nhân với 4 trạng thái tư thế công thái học chuẩn mực.", "1. Về dữ liệu: ")
    add_bullet_point(doc, "Đề xuất thành công pipeline trích xuất 12 đặc trưng hình học RAW12 kết hợp cơ chế Personal Baseline Calibration 30 mẫu, chuyển đổi sang không gian đặc trưng tương đối REP13 giúp giảm 33.8% độ phân tán giữa các cá nhân.", "2. Về thuật toán: ")
    add_bullet_point(doc, "Huấn luyện và đánh giá công bằng 4 thuật toán Machine Learning qua Nested LOPO CV; mô hình SVM RBF xuất sắc dẫn đầu với Macro F1 0.9199 và Accuracy 0.9329.", "3. Về mô hình AI: ")
    add_bullet_point(doc, "Triển khai hoàn chỉnh ứng dụng Web Dashboard thời gian thực trên nền FastAPI, WebSocket và TailwindCSS, xử lý mượt mà 15-22 FPS trên CPU văn phòng, tích hợp cảnh báo thông minh và xuất báo cáo lịch sử.", "4. Về ứng dụng: ")

    add_styled_heading(doc, "8.2. Những đóng góp nổi bật của đề tài", level=2)
    add_body_paragraph(doc, "Đề tài mang lại 3 đóng góp kỹ thuật quan trọng:")
    add_bullet_point(doc, "Giải quyết triệt để rào cản sai khác hình thể người dùng mà không cần huấn luyện lại mô hình.", "• Cơ chế Personal Baseline Calibration: ")
    add_bullet_point(doc, "Triệt tiêu hiện tượng rung giật nhãn và loại bỏ 100% cảnh báo giả khi người dùng quay mặt giao tiếp.", "• Bộ lọc kép Yaw Gating + Hysteresis: ")
    add_bullet_point(doc, "Triệt tiêu nguy cơ nghẽn hàng đợi (Backlog Queuing), giữ độ trễ luôn ổn định dưới 50ms và bảo đảm bảo mật dữ liệu tuyệt đối.", "• Kỹ thuật One-Frame-in-Flight WebSocket & Offline Processing: ")

    add_styled_heading(doc, "8.3. Hạn chế và Hướng phát triển tiếp theo", level=2)
    add_body_paragraph(doc, "Nhóm định hướng phát triển hệ thống trong tương lai theo các hướng:")
    add_bullet_point(doc, "Bổ sung mẫu dữ liệu ở nhiều điều kiện chiếu sáng và góc đặt camera khác nhau (trực diện, nghiêng 30°, nghiêng 60°).", "• Tự do hóa góc đặt camera: ")
    add_bullet_point(doc, "Bổ sung nhận diện các thói quen xấu phổ biến khác như chống cằm một tay, ngửa đầu ra sau, hoặc bắt chéo chân.", "• Mở rộng danh mục tư thế: ")
    add_bullet_point(doc, "Phát triển phiên bản ứng dụng chạy ngầm trên khay hệ thống (System Tray Desktop App bằng Electron / PyQt) và thông báo nhắc nhở qua Windows Notification.", "• Ứng dụng Desktop chạy nền: ")

    # =========================================================================
    # CHƯƠNG 9. ỨNG DỤNG AI TRONG QUÁ TRÌNH THỰC HIỆN ĐỀ TÀI
    # =========================================================================
    add_styled_heading(doc, "CHƯƠNG 9. ỨNG DỤNG AI TRONG QUÁ TRÌNH THỰC HIỆN ĐỀ TÀI", level=1)
    add_body_paragraph(doc, "Trong quá trình nghiên cứu và thực hiện đề tài, nhóm đã chủ động ứng dụng các công cụ Trí tuệ nhân tạo tạo sinh (Generative AI) như Google Gemini và OpenAI ChatGPT với vai trò là trợ lý kỹ thuật hỗ trợ nâng cao hiệu suất làm việc:")
    
    add_caption(doc, "Bảng 9.1: Bảng tổng hợp vai trò và phương thức kiểm chứng công cụ AI trong quá trình thực hiện.", is_table=True)
    create_table_from_data(doc, TABLE_AI_APPLICATIONS, col_widths=[1.5, 2.0, 1.9, 2.0], align_center_cols=[0])
    
    add_body_paragraph(doc, "Cam kết về liêm chính học thuật: Các thành viên trong nhóm luôn giữ vững vai trò chủ đạo trong việc ra quyết định kiến trúc, tự mình thu thập dữ liệu thực tế, thiết kế các công thức toán học và kiểm chứng độc lập mọi dòng mã nguồn trước khi đưa vào sản phẩm cuối cùng.")

    # =========================================================================
    # TÀI LIỆU THAM KHẢO
    # =========================================================================
    add_styled_heading(doc, "TÀI LIỆU THAM KHẢO", level=1)
    references = [
        "[1] Jocher, G., Chaurasia, A., & Qiu, J. (2023). Ultralytics YOLOv8 (Version 8.0.0). GitHub repository: https://github.com/ultralytics/ultralytics.",
        "[2] Cortes, C., & Vapnik, V. (1995). Support-vector networks. Machine Learning, 20(3), 273-297.",
        "[3] Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825-2830.",
        "[4] Lugaresi, C., et al. (2019). MediaPipe: A Framework for Building Perception Pipelines. arXiv preprint arXiv:1906.08172.",
        "[5] Hansraj, K. K. (2014). Assessment of stresses in the cervical spine caused by posture and position of the head. Surgical Technology International, 25, 277-279.",
        "[6] Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 785-794.",
        "[7] Tiangolo, S. (2018). FastAPI: Modern, fast (high-performance), web framework for building APIs with Python 3.8+. https://fastapi.tiangolo.com/.",
        "[8] Grandjean, E. (1987). Ergonomics in Computerized Offices. CRC Press, Taylor & Francis Group."
    ]
    for ref in references:
        p_ref = doc.add_paragraph()
        p_ref.paragraph_format.space_before = Pt(2)
        p_ref.paragraph_format.space_after = Pt(4)
        p_ref.paragraph_format.line_spacing = 1.2
        r_ref = p_ref.add_run(ref)
        r_ref.font.name = "Times New Roman"
        r_ref.font.size = Pt(11)
        r_ref.font.color.rgb = RGB_TEXT_BLACK

    # =========================================================================
    # PHỤ LỤC. THÔNG TIN KỸ THUẬT BỔ SUNG
    # =========================================================================
    add_styled_heading(doc, "PHỤ LỤC. THÔNG TIN KỸ THUẬT BỔ SUNG", level=1)
    
    # Phụ lục A
    add_styled_heading(doc, "Phụ lục A. Danh mục chi tiết các đặc trưng hình học (RAW12 & REP13)", level=2)
    add_body_paragraph(doc, "Phụ lục A cung cấp định nghĩa chi tiết của 12 đặc trưng hình học thô (RAW12) và 13 đặc trưng đại diện tương đối (REP13) sử dụng trong toàn bộ hệ thống:")
    add_caption(doc, "Bảng A.1: Bảng đặc tả chi tiết 12 đặc trưng hình học thô cơ sở (RAW12).", is_table=True)
    create_table_from_data(doc, TABLE_RAW12_SPEC, col_widths=[0.8, 1.8, 1.2, 1.4, 0.6, 1.6], align_center_cols=[0, 4])
    add_caption(doc, "Bảng A.2: Bảng đặc tả chi tiết 13 đặc trưng đại diện tương đối chuẩn hóa (REP13).", is_table=True)
    create_table_from_data(doc, TABLE_REP13_SPEC, col_widths=[0.8, 2.0, 0.9, 1.5, 0.8, 1.4], align_center_cols=[0, 2])

    # Phụ lục B
    add_styled_heading(doc, "Phụ lục B. Cấu hình huấn luyện và không gian tìm kiếm siêu tham số", level=2)
    add_body_paragraph(doc, "Phụ lục B tổng hợp toàn bộ không gian siêu tham số thử nghiệm, cấu hình chốt cho Production và thông số phần cứng thực nghiệm:")
    add_caption(doc, "Bảng B.1: Không gian tìm kiếm siêu tham số (Grid Search Space) của 4 thuật toán học máy.", is_table=True)
    create_table_from_data(doc, HYPERPARAMETER_SEARCH_SPACE, col_widths=[1.5, 1.8, 2.2, 1.9], align_center_cols=[0])
    add_caption(doc, "Bảng B.2: Bộ siêu tham số tối ưu chốt cho phiên bản Production của từng thuật toán.", is_table=True)
    create_table_from_data(doc, OPTIMAL_PARAMS, col_widths=[1.8, 3.4, 1.1, 1.1], align_center_cols=[0, 2, 3])
    add_caption(doc, "Bảng B.3: Thông số cấu hình phần cứng và môi trường thực nghiệm.", is_table=True)
    create_table_from_data(doc, HARDWARE_CONFIG, col_widths=[2.4, 5.0], align_center_cols=[0])

    # Phụ lục C
    add_styled_heading(doc, "Phụ lục C. Các đoạn mã nguồn trọng yếu của hệ thống", level=2)
    add_body_paragraph(doc, "Dưới đây là các đoạn mã nguồn cốt lõi đã được kiểm thử và vận hành thực tế trong hệ thống Smart Posture Monitor V03:")
    
    add_styled_heading(doc, "C.1. Module trích xuất đặc trưng hình học thô RAW12 (src/feature_extractor.py)", level=3)
    add_code_block(doc, CODE_SNIPPETS["feature_extractor"])

    add_styled_heading(doc, "C.2. Module tính toán Baseline cá nhân và Circular Median (src/personal_calibration.py)", level=3)
    add_code_block(doc, CODE_SNIPPETS["personal_calibration"])

    add_styled_heading(doc, "C.3. Module biến đổi không gian đặc trưng tương đối REP13 (src/representation_builder.py)", level=3)
    add_code_block(doc, CODE_SNIPPETS["representation_builder"])

    add_styled_heading(doc, "C.4. Module bộ lọc ổn định chuỗi thời gian và Yaw Gating (src/temporal_monitor.py)", level=3)
    add_code_block(doc, CODE_SNIPPETS["temporal_monitor"])

    add_styled_heading(doc, "C.5. Module tính Điểm Công thái học và Đợt vi phạm (src/session_statistics.py)", level=3)
    add_code_block(doc, CODE_SNIPPETS["session_statistics"])

    # Phụ lục D
    add_styled_heading(doc, "Phụ lục D. Kết quả thực nghiệm chi tiết từng Fold và từng cá nhân", level=2)
    add_body_paragraph(doc, "Bảng D.1 ghi nhận chi tiết kết quả huấn luyện và kiểm thử trên 14 Outer LOPO Folds của mô hình SVM RBF:")
    add_caption(doc, "Bảng D.1: Chi tiết kết quả 14 Outer LOPO Folds của mô hình SVM RBF.", is_table=True)
    create_table_from_data(doc, LOPO_FOLDS_SVM_RBF, col_widths=[0.8, 1.1, 0.8, 0.7, 1.9, 0.8, 0.8, 0.8, 0.8, 0.8], align_center_cols=[0, 1, 2, 3, 5, 6, 7, 8, 9])
    
    add_body_paragraph(doc, "Bảng D.2 đối sánh điểm Macro F1 trên từng cá nhân giữa 4 thuật toán Machine Learning:")
    add_caption(doc, "Bảng D.2: Bảng đối sánh Macro F1 của 14 cá nhân giữa 4 thuật toán Machine Learning.", is_table=True)
    create_table_from_data(doc, PER_PERSON_COMPARISON, col_widths=[1.1, 0.9, 0.9, 0.9, 0.9, 0.9, 1.8], align_center_cols=[0, 1, 2, 3, 4, 5])

    # Phụ lục E
    add_styled_heading(doc, "Phụ lục E. Cấu trúc mã nguồn Repository và Hướng dẫn triển khai", level=2)
    add_body_paragraph(doc, "Cấu trúc cây thư mục của dự án Smart Posture Monitor V03:")
    repo_tree = """smart-posture-monitor-V03/
├── app/
│   ├── app.py                     # FastAPI WebSocket & REST API Server
│   └── static/
│       └── index.html             # Giao diện Web Dashboard (Shadcn UI + TailwindCSS)
├── docs/                          # Tài liệu nghiên cứu, kiến trúc và báo cáo
│   ├── BAO_CAO_BAI_TAP_LON_SMART_POSTURE_MONITOR.docx
│   └── BAO_CAO_BAI_TAP_LON_SMART_POSTURE_MONITOR.md
├── models/                        # Trọng số mô hình đã huấn luyện
│   ├── best_model.joblib          # Mô hình SVM RBF chiến thắng tối ưu
│   ├── calibration_config.json    # Cấu hình 30 mẫu correct Baseline
│   ├── training_metadata.json     # Metadata chi tiết các chỉ số LOPO
│   └── yolo26n-pose.pt            # Mô hình YOLOv8-Pose Nano
├── results/                       # Kết quả thực nghiệm và ma trận nhầm lẫn
│   └── v03_lopo/
├── src/                           # Mã nguồn nghiệp vụ lõi
│   ├── feature_extractor.py       # Trích xuất RAW12
│   ├── personal_calibration.py    # Xây dựng Baseline & Circular Median
│   ├── representation_builder.py  # Biến đổi sang REP13
│   ├── posture_predictor.py       # Suy luận mô hình SVM
│   ├── temporal_monitor.py        # Làm mượt Majority Vote & Yaw Gating
│   └── session_statistics.py      # Đo thời gian & Tính Ergonomics Score
├── tests/                         # Bộ kiểm thử tự động (8 test suites)
├── requirements.txt               # Danh sách thư viện phụ thuộc
└── README.md                      # Hướng dẫn tổng quan dự án
"""
    add_code_block(doc, repo_tree)

    add_body_paragraph(doc, "Hướng dẫn cài đặt môi trường và khởi chạy ứng dụng Web Dashboard:")
    guide_text = """# 1. Khởi tạo môi trường ảo Python 3.10+
python -m venv .venv
.venv\\Scripts\\activate   # Trên Windows

# 2. Cài đặt các thư viện phụ thuộc
pip install -r requirements.txt

# 3. Khởi chạy máy chủ Web Dashboard
python -m uvicorn app.app:app --host 0.0.0.0 --port 8000 --reload

# 4. Truy cập ứng dụng trên trình duyệt web:
# Mở trình duyệt và truy cập địa chỉ: http://localhost:8000

# 5. Chạy bộ kiểm thử tự động xác thực hệ thống:
pytest tests/ -v
"""
    add_code_block(doc, guide_text)

    # 4. Lưu tài liệu
    os.makedirs("docs", exist_ok=True)
    out_docx_path = "docs/BAO_CAO_BAI_TAP_LON_SMART_POSTURE_MONITOR.docx"
    doc.save(out_docx_path)
    print(f"Đã lưu thành công file Word tại: {out_docx_path}")
    
    # Copy file ra Desktop cho người dùng
    desktop_docx_path = "c:/Users/win10/Desktop/BAO_CAO_BAI_TAP_LON_SMART_POSTURE_MONITOR.docx"
    shutil.copy2(out_docx_path, desktop_docx_path)
    print(f"Đã sao chép trực tiếp file Word ra Desktop: {desktop_docx_path}")

    return out_docx_path

if __name__ == "__main__":
    build_docx_report()
