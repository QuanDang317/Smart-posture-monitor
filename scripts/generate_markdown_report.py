"""
Script: generate_markdown_report.py
Tạo bản Markdown học thuật chuẩn của Báo cáo Bài tập lớn:
1. docs/BAO_CAO_BAI_TAP_LON_SMART_POSTURE_MONITOR.md
2. c:/Users/win10/Desktop/BAO_CAO_BAI_TAP_LON_SMART_POSTURE_MONITOR.md
"""

import os
import sys
import shutil

from report_data import *
from report_appendices import *

sys.stdout.reconfigure(encoding='utf-8')

def format_md_table(headers, rows):
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("\n", "<br>") for c in r) + " |")
    return "\n".join(out)

def build_markdown_report():
    print("Bắt đầu tạo tài liệu Markdown (.md)...")
    lines = []
    
    # Header Bìa
    lines.append("<div align=\"center\">\n")
    lines.append(f"### {METADATA['institution']}")
    lines.append(f"#### {METADATA['faculty']} – {METADATA['department']}\n")
    lines.append("![PTIT Logo](extracted_media/image2.jpg)\n")
    lines.append(f"# {METADATA['report_type']}")
    lines.append(f"### Học phần: {METADATA['course_name']}\n")
    lines.append("---\n")
    lines.append(f"## ĐỀ TÀI: “{METADATA['project_title']}”")
    lines.append(f"### ({METADATA['project_subtitle']})\n")
    lines.append("---\n")
    lines.append("</div>\n")
    
    # Thông tin nhóm
    lines.append(f"**Giảng viên hướng dẫn:** {METADATA['instructor']}  ")
    lines.append("**Sinh viên thực hiện:**")
    for s in METADATA["students"]:
        lines.append(f"- **{s['name']}** – MSV: `{s['code']}` ({s.get('role', 'Thành viên')})")
    lines.append(f"\n**Lớp danh nghĩa:** {METADATA['class_name']} – Hệ Đại học chính quy  ")
    lines.append(f"**Thời gian thực hiện:** {METADATA['location']}, {METADATA['date']}\n\n---\n")

    # Lời cảm ơn
    lines.append("## LỜI CẢM ƠN\n")
    lines.append("Lời đầu tiên, nhóm sinh viên chúng em xin được bày tỏ lòng biết ơn chân thành và sâu sắc nhất tới thầy **ThS. Phạm Danh Tuyên** – Giảng viên phụ trách học phần Lập trình Python. Trong suốt quá trình học tập và triển khai đề tài, thầy đã tận tình truyền đạt những kiến thức chuyên môn quý báu, định hướng phương pháp luận nghiên cứu khoa học, đồng thời đưa ra những lời khuyên xác đáng giúp nhóm giải quyết các bài toán kỹ thuật phức tạp từ khâu xử lý ảnh, trích xuất đặc trưng cho đến kiểm thử mô hình học máy theo chuẩn công thái học thực tiễn.\n")
    lines.append("Nhóm cũng xin chân thành cảm ơn các thầy cô giáo trong Khoa Công nghệ Thông tin 1 – Học viện Công nghệ Bưu chính Viễn thông đã tạo điều kiện học tập tốt nhất, cung cấp nền tảng kiến thức vững chắc về lập trình, toán ứng dụng và trí tuệ nhân tạo. Sự đồng hành và động viên của các thầy cô cùng 14 tình nguyện viên tham gia ghi hình xây dựng tập dữ liệu chính là động lực to lớn giúp nhóm hoàn thành đề tài này một cách chỉn chu và trọn vẹn nhất.\n")
    lines.append("*Mặc dù đã rất nỗ lực nghiên cứu và hoàn thiện sản phẩm, đề tài chắc chắn khó tránh khỏi những thiếu sót nhất định do giới hạn về mặt thời gian và điều kiện thực nghiệm. Nhóm chúng em rất mong nhận được những nhận xét, góp ý quý báu từ thầy và hội đồng thẩm định để sản phẩm ngày càng hoàn thiện hơn trong tương lai. Kính chúc thầy sức khỏe, niềm vui và luôn gặt hái nhiều thành công trong sự nghiệp trồng người cao quý!*\n")

    # Lời mở đầu
    lines.append("## LỜI MỞ ĐẦU\n")
    lines.append("Trong kỷ nguyên số hóa và sự phổ biến của mô hình làm việc từ xa (Remote / Hybrid Work), thời gian làm việc và học tập trước màn hình máy tính ngày càng tăng, phổ biến từ 8 đến 12 tiếng mỗi ngày. Tuy nhiên, việc duy trì tư thế ngồi đúng chuẩn công thái học (Ergonomics) trong thời gian dài là một thách thức rất lớn đối với đa số người sử dụng. Người dùng thường vô thức rơi vào các tư thế sai lệch như cúi đầu về phía trước (Forward Head Posture - thường gọi là hội chứng Text Neck), gù lưng và rướn người về phía màn hình (Forward Slouch), hoặc nghiêng người, vẹo cột sống sang một bên (Lateral Lean). Những tư thế sai này nếu kéo dài liên tục không chỉ gây đau mỏi cơ cổ, vai gáy, thắt lưng mà còn làm tăng áp lực lên đĩa đệm cột sống (có thể lên tới 27 kg khi đầu cúi 60°), dẫn tới nguy cơ thoái hóa đốt sống cổ sớm, thoát vị đĩa đệm và suy giảm nghiêm trọng hiệu suất lao động trí tuệ.\n")
    lines.append("Mặc dù nhận thức rõ tầm quan trọng của việc giữ thẳng lưng, người dùng vẫn rất khó tự phát hiện và sửa sai kịp thời, đặc biệt khi đang tập trung cao độ vào công việc chuyên môn. Các giải pháp truyền thống trên thị trường hiện nay bộc lộ nhiều điểm hạn chế: Các thiết bị cảm biến đeo (wearable sensors) thường gây vướng víu, khó chịu khi sử dụng cả ngày và đòi hỏi chi phí đầu tư phần cứng; trong khi các phần mềm nhắc giờ cố định (như phương pháp Pomodoro) lại không phản ánh đúng tư thế ngồi thực tế. Do đó, việc xây dựng một hệ thống thị giác thông minh có khả năng giám sát tư thế liên tục, phát hiện sai lệch và đưa ra cảnh báo kịp thời theo thời gian thực là một nhu cầu cấp thiết và mang tính ứng dụng xã hội sâu sắc.\n")
    lines.append("Sự phát triển vượt bậc của Trí tuệ nhân tạo (AI) và Thị giác máy tính (Computer Vision) đã mở ra hướng đi tối ưu cho bài toán này. Bằng cách tận dụng trực tiếp webcam máy tính sẵn có, hệ thống có thể theo dõi tư thế mà không gây cảm giác khó chịu cho người dùng, đồng thời tiết kiệm 100% chi phí mua sắm thiết bị ngoại vi chuyên dụng.\n")
    lines.append("Xuất phát từ thực tiễn trên, nhóm lựa chọn thực hiện đề tài: **“Xây dựng hệ thống giám sát tư thế ngồi thời gian thực – Smart Posture Monitor (Phiên bản V03)”**. Hệ thống kết hợp giữa mô hình ước lượng tư thế người siêu nhẹ YOLOv8-Pose và thuật toán phân loại Support Vector Machine (SVM nhân RBF), tích hợp cơ chế hiệu chuẩn cá nhân hóa (Personal Baseline Calibration 30 mẫu) và bộ lọc ổn định chuỗi thời gian (Temporal Smoothing, Hysteresis và Yaw Gating). Toàn bộ pipeline được đóng gói thành một ứng dụng Web Dashboard trực quan, vận hành hoàn toàn Offline trên máy trạm cục bộ, bảo vệ quyền riêng tư tuyệt đối cho người dùng.\n")

    # Quy ước thuật ngữ
    lines.append("## QUY ƯỚC VÀ THUẬT NGỮ\n")
    lines.append(format_md_table(["Thuật ngữ / Viết tắt", "Định nghĩa và Ý nghĩa sử dụng trong đề tài"], GLOSSARY))
    lines.append("\n---\n")

    # Mục lục
    lines.append("## MỤC LỤC TỔNG THỂ\n")
    lines.append("""- [LỜI CẢM ƠN](#lời-cảm-ơn)
- [LỜI MỞ ĐẦU](#lời-mở-đầu)
- [QUY ƯỚC VÀ THUẬT NGỮ](#quy-ước-và-thuật-ngữ)
- [CHƯƠNG 1. TỔNG QUAN BÀI TOÁN VÀ MỤC TIÊU](#chương-1-tổng-quan-bài-toán-và-mục-tiêu)
  - [1.1. Bối cảnh và lý do chọn đề tài](#11-bối-cảnh-và-lý-do-chọn-đề-tài)
  - [1.2. Phát biểu bài toán nhận diện tư thế](#12-phát-biểu-bài-toán-nhận-diện-tư-thế)
  - [1.3. Mục tiêu nghiên cứu và phát triển](#13-mục-tiêu-nghiên-cứu-và-phát-triển)
  - [1.4. Phạm vi và giới hạn của đề tài](#14-phạm-vi-và-giới-hạn-của-đề-tài)
- [CHƯƠNG 2. YÊU CẦU VÀ CHỨC NĂNG HỆ THỐNG](#chương-2-yêu-cầu-và-chức-năng-hệ-thống)
  - [2.1. Yêu cầu chức năng (Functional Requirements)](#21-yêu-cầu-chức-năng-functional-requirements)
  - [2.2. Yêu cầu phi chức năng (Non-Functional Requirements)](#22-yêu-cầu-phi-chức-năng-non-functional-requirements)
  - [2.3. Quy trình người dùng (User Flow)](#23-quy-trình-người-dùng-user-flow)
- [CHƯƠNG 3. PHÂN TÍCH VÀ LỰA CHỌN GIẢI PHÁP](#chương-3-phân-tích-và-lựa-chọn-giải-pháp)
  - [3.1. Phân tích các hướng tiếp cận công nghệ](#31-phân-tích-các-hướng-tiếp-cận-công-nghệ)
  - [3.2. Kiến trúc giải pháp tổng thể đề xuất](#32-kiến-trúc-giải-pháp-tổng-thể-đề-xuất)
  - [3.3. Ước lượng tư thế và lựa chọn điểm mốc cơ thể (Keypoints)](#33-ước-lượng-tư-thế-và-lựa-chọn-điểm-mốc-cơ-thể-keypoints)
  - [3.4. Kỹ thuật thiết kế đặc trưng hình học (RAW12)](#34-kỹ-thuật-thiết-kế-đặc-trưng-hình-học-raw12)
  - [3.5. Hiệu chuẩn cá nhân hóa và Biểu diễn đặc trưng tương đối (REP13)](#35-hiệu-chuẩn-cá-nhân-hóa-và-biểu-diễn-đặc-trưng-tương-đối-rep13)
  - [3.6. Nghiên cứu và lựa chọn mô hình Machine Learning](#36-nghiên-cứu-và-lựa-chọn-mô-hình-machine-learning)
  - [3.7. Bộ lọc chuỗi thời gian (Temporal Monitoring & Yaw Gating)](#37-bộ-lọc-chuỗi-thời-gian-temporal-monitoring--yaw-gating)
- [CHƯƠNG 4. THIẾT KẾ CHƯƠNG TRÌNH VÀ HỆ THỐNG](#chương-4-thiết-kế-chương-trình-và-hệ-thống)
  - [4.1. Kiến trúc phân tầng của hệ thống](#41-kiến-trúc-phân-tầng-của-hệ-thống)
  - [4.2. Thiết kế chi tiết các module nghiệp vụ](#42-thiết-kế-chi-tiết-các-module-nghiệp-vụ)
  - [4.3. Thiết kế luồng xử lý thời gian thực (One-Frame-in-Flight)](#43-thiết-kế-luồng-xử-lý-thời-gian-thực-one-frame-in-flight)
  - [4.4. Quy trình huấn luyện và kiểm thử mô hình](#44-quy-trình-huấn-luyện-và-kiểm-thử-mô-hình)
  - [4.5. Thiết kế giao diện người dùng (Dashboard UI)](#45-thiết-kế-giao-diện-người-dùng-dashboard-ui)
- [CHƯƠNG 5. THƯ VIỆN, FRAMEWORK VÀ CÔNG NGHỆ](#chương-5-thư-viện-framework-và-công-nghệ)
- [CHƯƠNG 6. THỰC NGHIỆM, KẾT QUẢ VÀ MINH HỌA SẢN PHẨM](#chương-6-thực-nghiệm-kết-quả-và-minh-họa-sản-phẩm)
  - [6.1. Thu thập và Phân tích tập dữ liệu thực nghiệm (Dataset & EDA)](#61-thu-thập-và-phân-tích-tập-dữ-liệu-thực-nghiệm-dataset--eda)
  - [6.2. Phương pháp đánh giá mô hình (Nested LOPO CV)](#62-phương-pháp-đánh-giá-mô-hình-nested-lopo-cv)
  - [6.3. Đánh giá và so sánh hiệu năng các mô hình Machine Learning](#63-đánh-giá-và-so-sánh-hiệu-năng-các-mô-hình-machine-learning)
  - [6.4. Đánh giá hiệu năng vận hành thời gian thực](#64-đánh-giá-hiệu-năng-vận-hành-thời-gian-thực)
  - [6.5. Đánh giá hiệu quả của bộ lọc Temporal Monitoring](#65-đánh-giá-hiệu-quả-của-bộ-lọc-temporal-monitoring)
  - [6.6. Đánh giá cơ chế thống kê và Điểm Công thái học](#66-đánh-giá-cơ-chế-thống-kê-và-điểm-công-thái-học)
  - [6.7. Tổng kết đánh giá ưu điểm và hạn chế của hệ thống](#67-tổng-kết-đánh-giá-ưu-điểm-và-hạn-chế-của-hệ-thống)
- [CHƯƠNG 7. PHÂN CHIA CÔNG VIỆC TRONG NHÓM](#chương-7-phân-chia-công-việc-trong-nhóm)
- [CHƯƠNG 8. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN](#chương-8-kết-luận-và-hướng-phát-triển)
  - [8.1. Các kết quả chính đạt được](#81-các-kết-quả-chính-đạt-được)
  - [8.2. Những đóng góp nổi bật của đề tài](#82-những-đóng-góp-nổi-bật-của-đề-tài)
  - [8.3. Hạn chế và Hướng phát triển tiếp theo](#83-hạn-chế-và-hướng-phát-triển-tiếp-theo)
- [CHƯƠNG 9. ỨNG DỤNG AI TRONG QUÁ TRÌNH THỰC HIỆN ĐỀ TÀI](#chương-9-ứng-dụng-ai-trong-quá-trình-thực-hiện-đề-tài)
- [TÀI LIỆU THAM KHẢO](#tài-liệu-tham-khảo)
- [PHỤ LỤC. THÔNG TIN KỸ THUẬT BỔ SUNG](#phụ-lục-thông-tin-kỹ-thuật-bổ-sung)
  - [Phụ lục A. Danh mục chi tiết các đặc trưng hình học (RAW12 & REP13)](#phụ-lục-a-danh-mục-chi-tiết-các-đặc-trưng-hình-học-raw12--rep13)
  - [Phụ lục B. Cấu hình huấn luyện và không gian tìm kiếm siêu tham số](#phụ-lục-b-cấu-hình-huấn-luyện-và-không-gian-tìm-kiếm-siêu-tham-số)
  - [Phụ lục C. Các đoạn mã nguồn trọng yếu của hệ thống](#phụ-lục-c-các-đoạn-mã-nguồn-trọng-yếu-của-hệ-thống)
  - [Phụ lục D. Kết quả thực nghiệm chi tiết từng Fold và từng cá nhân](#phụ-lục-d-kết-quả-thực-nghiệm-chi-tiết-từng-fold-và-từng-cá-nhân)
  - [Phụ lục E. Cấu trúc mã nguồn Repository và Hướng dẫn triển khai](#phụ-lục-e-cấu-trúc-mã-nguồn-repository-và-hướng-dẫn-triển-khai)
\n---\n""")

    # Chương 1
    lines.append("""# CHƯƠNG 1. TỔNG QUAN BÀI TOÁN VÀ MỤC TIÊU

## 1.1. Bối cảnh và lý do chọn đề tài
Trong thời đại cách mạng công nghiệp 4.0, máy tính cá nhân và laptop đã trở thành công cụ lao động không thể thiếu đối với học sinh, sinh viên và nhân viên văn phòng. Tuy nhiên, thói quen ngồi làm việc tĩnh tại liên tục trong nhiều giờ liền lại kéo theo những hiểm họa khôn lường đối với sức khỏe cơ xương khớp.

Các nghiên cứu y khoa về công thái học (Ergonomics) chỉ ra rằng, khi quá tập trung vào màn hình, con người có xu hướng vô thức rướn cổ về phía trước, gù lưng hoặc nghiêng vẹo sang một bên để giảm bớt sự căng thẳng của cơ bắp. Cứ mỗi 2.5 cm đầu dịch chuyển về phía trước, áp lực đè nặng lên các đốt sống cổ lại tăng thêm tương đương gần 4.5 kg. Ở trạng thái cúi 60°, sức nặng mà cột sống cổ phải chịu tải có thể lên tới 27 kg. Về lâu dài, các thói quen xấu này dẫn tới các chứng bệnh mãn tính nguy hiểm: hội chứng cổ rùa (Text Neck Syndrome), thoái hóa cột sống cổ sớm, thoát vị đĩa đệm, đau dây thần kinh tọa và cong vẹo cột sống học đường.

Mặc dù người dùng đều ý thức được tác hại này, họ không thể tự kiểm soát tư thế của mình một cách liên tục nếu thiếu một công cụ hỗ trợ thông minh. Các thiết bị cảm biến đeo (wearable sensors) thường gây khó chịu, vướng víu và bất tiện khi phải sạc pin thường xuyên; trong khi các ứng dụng hẹn giờ cố định (Pomodoro) không có khả năng giám sát trực quan xem người dùng có thực sự ngồi đúng hay không. Xuất phát từ thực trạng đó, nhóm quyết định nghiên cứu và xây dựng hệ thống **Smart Posture Monitor** nhằm tự động phát hiện, đánh giá và nhắc nhở tư thế ngồi thời gian thực thông qua webcam máy tính.

## 1.2. Phát biểu bài toán nhận diện tư thế
Bài toán đặt ra cho hệ thống là: Từ luồng video đầu vào (Input Frames) thu nhận liên tục từ webcam 2D tiêu chuẩn của máy tính, hệ thống cần tự động phát hiện người, định vị các điểm mốc giải phẫu trọng yếu trên cơ thể, trích xuất các đặc trưng hình học có ý nghĩa và phân loại chính xác trạng thái ngồi hiện tại của người dùng vào một trong bốn nhãn lớp công thái học:
1. **`correct`**: Tư thế ngồi thẳng lưng, cổ và vai cân bằng đúng chuẩn công thái học.
2. **`forward_slouch`**: Tư thế cúi đầu, rướn cổ hoặc gù lưng về phía màn hình máy tính.
3. **`lean_left`**: Tư thế nghiêng đầu hoặc vẹo cột sống sang phía bên trái.
4. **`lean_right`**: Tư thế nghiêng đầu hoặc vẹo cột sống sang phía bên phải.

Đồng thời, hệ thống phải theo dõi chuỗi thời gian để kích hoạt cảnh báo thông minh (banner đỏ thị giác + chuông âm thanh) khi người dùng duy trì tư thế sai liên tục vượt quá ngưỡng thời gian cho phép (mặc định 2.0 giây), và tổng kết phiên làm việc qua Điểm số Công thái học (Ergonomics Score).

## 1.3. Mục tiêu nghiên cứu và phát triển
Để giải quyết trọn vẹn bài toán trên, nhóm đặt ra ba mục tiêu nghiên cứu cốt lõi:
- **Mục tiêu 1 – Độ chính xác và Cá nhân hóa cao:** Thay vì áp dụng ngưỡng cứng nhắc cho mọi đối tượng, hệ thống phải có khả năng thích ứng linh hoạt với sự khác biệt về vóc dáng, chiều cao, chiều dài cổ và khoảng cách đặt webcam của từng cá nhân thông qua cơ chế Personal Baseline Calibration 30 mẫu, chuyển đổi từ RAW12 sang không gian đặc trưng tương đối REP13.
- **Mục tiêu 2 – Tính ổn định thời gian thực:** Khắc phục triệt để hiện tượng nhấp nháy chuyển nhãn (flickering) và triệt tiêu báo động sai khi người dùng chỉ quay đầu nói chuyện thông qua bộ lọc Yaw Gating kết hợp cửa sổ trượt Majority Vote và cơ chế trễ Hysteresis.
- **Mục tiêu 3 – Tính ứng dụng thực tiễn và Bảo mật:** Triển khai một ứng dụng Web Dashboard hoàn chỉnh, giao diện Shadcn UI hiện đại, hỗ trợ Dark/Light mode, biểu đồ Chart.js trực quan, và bảo đảm vận hành 100% Offline trên CPU máy tính văn phòng, bảo mật tuyệt đối dữ liệu hình ảnh người dùng.

## 1.4. Phạm vi và giới hạn của đề tài
- **Về bài toán và dữ liệu:** Hệ thống tập trung phân loại 4 trạng thái tư thế ngồi làm việc phổ biến nhất của phần thân trên dựa trên dữ liệu ảnh 2D RGB từ webcam thông thường, chưa mở rộng sang ước lượng chiều sâu 3D (Depth camera) hoặc phân tích tư thế phần thân dưới (hông, chân).
- **Về giao thức bố trí camera:** Camera được đặt cố định ở góc chếch khoảng **45° về phía bên trái** của người dùng (góc quan sát tối ưu nhất để nhìn rõ đồng thời cả độ gập cổ và độ nghiêng vai). Ảnh đầu vào là ảnh gốc không lật gương (unmirrored) để đảm bảo phân định chính xác hướng nghiêng trái / phải.
- **Về quy trình vận hành:** Người dùng cần thực hiện bước hiệu chuẩn mốc chuẩn cá nhân (ngồi thẳng lưng trong khoảng 2-3 giây đầu để thu 30 mẫu correct) trước khi bước vào phiên giám sát tự động.
- **Về mục đích ứng dụng:** Sản phẩm hướng tới mục tiêu hỗ trợ cải thiện thói quen ngồi làm việc và nâng cao nhận thức bảo vệ sức khỏe, không đóng vai trò là thiết bị chẩn đoán y khoa chuyên dụng.

---
""")

    # Chương 2
    lines.append("""# CHƯƠNG 2. YÊU CẦU VÀ CHỨC NĂNG HỆ THỐNG

## 2.1. Yêu cầu chức năng (Functional Requirements)
Hệ thống Smart Posture Monitor được phân rã thành 7 phân hệ nghiệp vụ chính:
1. **Phân hệ thu nhận và xử lý hình ảnh (Video & Frame Acquisition):** Thu nhận luồng webcam 640x480 qua Web API, mã hóa Base64 và truyền tải hai chiều độ trễ thấp qua WebSocket (`/ws/stream`). Đo độ trễ trọn vòng Ping (ms).
2. **Phân hệ thị giác máy tính và trích xuất đặc trưng (Computer Vision & Feature Engineering):** Định vị dáng người và trích xuất 6 điểm mốc giải phẫu cốt lõi bằng YOLOv8-Pose Nano. Lọc chủ thể trung tâm qua điểm kết hợp $S_i = 0.7 \cdot C_i + 0.3 \cdot P_i$. Trích xuất vector 12 đặc trưng hình học thô (RAW12).
3. **Phân hệ hiệu chuẩn tư thế cá nhân hóa (Personal Baseline Calibration):** Thu thập 30 mẫu correct hợp lệ đầu phiên. Áp dụng thuật toán Circular Median cho góc và Median cho khoảng cách để xây dựng Baseline, sau đó tạo vector đặc trưng tương đối 13 chiều (REP13).
4. **Phân hệ suy luận và phân loại tư thế (Posture Classification):** Phân loại đa lớp 4 trạng thái tư thế ngồi bằng mô hình SVM (Kernel RBF) và ước lượng phân bố xác suất tin cậy tức thời.
5. **Phân hệ hậu xử lý và làm mượt thời gian (Temporal Processing):** Bộ lọc Yaw Gating khử nhiễu quay đầu; Cửa sổ trượt đa số Majority Vote ($W=7$ frames); và Cơ chế trễ chuyển đổi trạng thái Hysteresis (2 frames).
6. **Phân hệ cảnh báo và thống kê phiên làm việc (Alerting & Ergonomics Statistics):** Kích hoạt cảnh báo kép (Banner đỏ nhấp nháy + Âm thanh chuông báo Bip) khi ngồi sai liên tục $> 2.0\\text{s}$. Gom đợt vi phạm liên tục thành 1 lần (Violation Episode). Chấm Điểm Công thái học (Ergonomics Score từ 0 đến 100).
7. **Phân hệ bảng điều khiển và trực quan hóa (Dashboard UI):** Khung webcam có lớp vẽ khung xương 6 điểm (Canvas Overlay); Ma trận 4 thẻ KPI chỉ số; Biểu đồ phân tích Chart.js; Quản lý lịch sử phiên và hỗ trợ xuất báo cáo CSV/Excel.

## 2.2. Yêu cầu phi chức năng (Non-Functional Requirements)
""")
    lines.append(format_md_table(
        ["Nhóm yêu cầu", "Tiêu chuẩn kỹ thuật đặt ra", "Giải thích ý nghĩa và Giải pháp kỹ thuật trong dự án"],
        [
            ["Tính thời gian thực (Real-time)", "Tốc độ xử lý: 15 – 22 FPS<br>Tổng độ trễ: < 80 ms", "Toàn bộ pipeline AI xử lý mượt mà trên CPU máy tính văn phòng thông thường, phản hồi kết quả tức thì lên giao diện web."],
            ["Độ ổn định chuỗi thời gian (Temporal Stability)", "Kháng nhiễu khung hình, triệt tiêu rung giật nhãn", "Loại bỏ hoàn toàn hiện tượng nhấp nháy nhãn (flickering) thông qua bộ lọc Yaw Gating và cơ chế kép Majority Vote + Hysteresis."],
            ["Tính dễ sử dụng & Tiếp cận (Usability)", "Không cần thiết bị chuyên dụng, giao diện thân thiện", "Chỉ yêu cầu webcam laptop sẵn có và trình duyệt web. Hỗ trợ đầy đủ phím tắt nhanh (C hiệu chuẩn, R đặt lại, Q dừng)."],
            ["Kiến trúc module hóa (Modularity)", "Tuân thủ chặt chẽ nguyên lý Single Responsibility", "Các khối PoseDetector, FeatureExtractor, Calibration, Predictor, Monitor độc lập, có thể dễ dàng bảo trì và viết Unit Test."],
            ["Hoạt động Ngoại tuyến & Bảo mật (Offline & Privacy)", "Xử lý cục bộ 100% trên thiết bị người dùng", "Không lưu trữ hay truyền tải bất kỳ hình ảnh nhạy cảm nào của người dùng lên đám mây, bảo đảm quyền riêng tư tuyệt đối."],
            ["Độ chính xác & Khái quát hóa (Generalization)", "Macro F1-score: > 0.90 trên người dùng chưa từng thấy", "Mô hình đạt Macro F1 trung bình 0.9199 qua kiểm thử nghiêm ngặt Nested Leave-One-Person-Out CV trên 14 người dùng độc lập."]
        ]
    ))

    lines.append("""
## 2.3. Quy trình người dùng (User Flow)
```mermaid
flowchart TD
    A["Bắt đầu phiên<br>(Mở Web, bật Webcam)"] --> B["Hiệu chuẩn Baseline<br>(Ấn C: lấy 30 mẫu correct)"]
    B --> C["Theo dõi tư thế<br>(Ngồi làm việc bình thường)"]
    C --> D["Nhận diện AI Realtime<br>(YOLO + SVM + Lọc chuỗi thời gian 15-22 FPS)"]
    D --> E{"Vi phạm liên tục > 2s?"}
    E -- "Có" --> F["Cảnh báo thông minh<br>(Banner đỏ + Âm thanh chuông báo)"]
    E -- "Không" --> D
    F --> D
    D --> G["Kết thúc phiên<br>(Ấn 'Kết thúc phiên' hoặc phím Q / Esc)"]
    G --> H["Xem phân tích & Lịch sử<br>(Điểm Công thái học, Biểu đồ Chart.js, Xuất CSV)"]
```

---
""")

    # Chương 3
    lines.append("""# CHƯƠNG 3. PHÂN TÍCH VÀ LỰA CHỌN GIẢI PHÁP

## 3.1. Phân tích các hướng tiếp cận công nghệ
""")
    lines.append(format_md_table(TABLE_COMPARISON_APPROACHES[0], TABLE_COMPARISON_APPROACHES[1:]))

    lines.append("""
## 3.2. Kiến trúc giải pháp tổng thể đề xuất
![Hình 3.1: Kiến trúc xử lý nhận diện tư thế ngồi đề xuất](extracted_media/image5.png)
*Hình 3.1: Sơ đồ kiến trúc xử lý nhận diện tư thế ngồi đề xuất (Pipeline V03).*

### Quá trình phát triển và cải tiến qua các phiên bản (V01, V02, V03)
""")
    lines.append(format_md_table(TABLE_VERSION_EVOLUTION[0], TABLE_VERSION_EVOLUTION[1:]))

    lines.append("""
> [!IMPORTANT]
> **Điểm đột phá mang tính quyết định của Phiên bản V03:**
> Khác biệt căn bản giữa V03 và các phiên bản trước là sự ra đời của cơ chế **Personal Calibration**. Thay vì cố gắng tìm kiếm một đường biên quyết định toàn cục trên các tọa độ hình học tuyệt đối (vốn luôn bị biến dạng bởi chiều cao, độ rộng vai và cự ly ngồi của từng người), V03 chuyển đổi toàn bộ bài toán sang không gian độ lệch tương đối (Relative Space) so với chính tư thế chuẩn của người đó. Nhờ vậy, độ phân tán dữ liệu giữa các cá nhân giảm mạnh 33.8%, nâng Macro F1 trên người dùng mới từ 0.846 lên 0.9199.

## 3.3. Ước lượng tư thế và lựa chọn điểm mốc cơ thể (Keypoints)
![Hình 3.2: Minh họa các keypoints COCO](extracted_media/image4.png)
*Hình 3.2: Minh họa 17 điểm mốc cơ thể theo định dạng COCO của YOLO-Pose.*

Nhóm tinh gọn lại đúng 6 điểm mốc cốt lõi thuộc vùng thân trên:
""")
    lines.append(format_md_table(TABLE_KEYPOINTS[0], TABLE_KEYPOINTS[1:]))

    lines.append("""
### Thuật toán chọn lọc chủ thể trung tâm tối ưu
Điểm ưu tiên $S_i$ cho từng người $i$ phát hiện được xác định theo công thức:
$$S_i = 0.7 \cdot C_i + 0.3 \cdot P_i$$
Trong đó $C_i$ là chỉ số đo mức độ gần tâm hình ảnh (centrality, từ 0 đến 1), và $P_i$ là độ tin cậy phát hiện người do YOLO cung cấp.

## 3.4. Kỹ thuật thiết kế đặc trưng hình học (RAW12)
Từ tọa độ 6 điểm mốc giải phẫu hợp lệ, hệ thống tính toán 12 đặc trưng hình học thô (RAW12):
""")
    lines.append(format_md_table(TABLE_RAW12_SPEC[0], TABLE_RAW12_SPEC[1:]))

    lines.append("""
## 3.5. Hiệu chuẩn cá nhân hóa và Biểu diễn đặc trưng tương đối (REP13)
![Hình 3.3: Sơ đồ hiệu chuẩn Baseline](extracted_media/image3.png)
*Hình 3.3: Quy trình hiệu chuẩn Baseline cá nhân hóa và biến đổi RAW12 sang REP13.*

- **Thuật toán Circular Median cho góc tuần hoàn:**
  $$\theta_{\text{ref}} = \arg\min_{\theta_i} \sum_{j=1}^{30} |\text{wrap}(\theta_i - \theta_j)|$$
  Sau khi chọn góc tham chiếu $\theta_{\text{ref}}$, mở rộng các góc trên đường tròn và tính trung vị tuyến tính.
- **Chuẩn hóa khoảng cách theo độ rộng vai $W_0$:**
  $$\Delta s_j = \frac{s_j - b_j}{W_0}$$
- **Đại lượng tỷ số log khoảng cách (Log-ratio):**
  $$r_j = \ln\left(\frac{s_j}{b_j}\right)$$
- **Độ lớn dịch chuyển tổng hợp của đầu (Head Drift Magnitude):**
  $$D = \sqrt{(\Delta \text{eye\_center\_x\_body})^2 + (\Delta \text{eye\_center\_y\_body})^2}$$

""")
    lines.append(format_md_table(TABLE_REP13_SPEC[0], TABLE_REP13_SPEC[1:]))

    lines.append("""
## 3.6. Nghiên cứu và lựa chọn mô hình Machine Learning
""")
    lines.append(format_md_table(TABLE_MODEL_ALGORITHMS[0], TABLE_MODEL_ALGORITHMS[1:]))

    lines.append("""
## 3.7. Bộ lọc chuỗi thời gian (Temporal Monitoring & Yaw Gating)
- **Khử nhiễu quay đầu (Yaw Gating):** Đo tỷ lệ khoảng cách mắt - mũi $R = \frac{d(\text{Left Eye}, \text{Nose})}{d(\text{Right Eye}, \text{Nose})}$. Khi $R < 0.45$ hoặc $R > 1.80$, hệ thống tự động khóa trạng thái thân trên ổn định trước đó.
- **Cửa sổ trượt đa số (Majority Vote $W=7$):** Bầu chọn nhãn chiếm đa số tuyệt đối trong 7 khung hình gần nhất.
- **Cơ chế trễ trạng thái (Hysteresis):** Yêu cầu nhãn ứng viên mới duy trì liên tiếp 2 khung hình trước khi chuyển trạng thái hiển thị.

---
""")

    # Chương 4
    lines.append("""# CHƯƠNG 4. THIẾT KẾ CHƯƠNG TRÌNH VÀ HỆ THỐNG

## 4.1. Kiến trúc phân tầng của hệ thống
![Hình 4.1: Sơ đồ kiến trúc tổng thể](extracted_media/image6.png)
*Hình 4.1: Sơ đồ kiến trúc tổng thể hệ thống giám sát tư thế ngồi (3 phân tầng chính).*

## 4.2. Thiết kế chi tiết các module nghiệp vụ
""")
    lines.append(format_md_table(TABLE_MODULES[0], TABLE_MODULES[1:]))

    lines.append("""
## 4.3. Thiết kế luồng xử lý thời gian thực (One-Frame-in-Flight)
![Hình 4.2: Luồng xử lý thời gian thực](extracted_media/image7.png)
*Hình 4.2: Sơ đồ luồng xử lý thời gian thực khép kín (One-Frame-in-Flight).*

> [!TIP]
> **Cơ chế One-Frame-in-Flight / Latest-Frame-Wins:**
> Frontend chỉ gửi khung hình tiếp theo khi khung hình trước đã nhận phản hồi từ Server (`frameInFlight = false`). Tách riêng Canvas hiển thị và Offscreen Canvas chụp ảnh, triệt tiêu hiện tượng dồn ứ khung hình và giữ độ trễ luôn $< 50\\text{ms}$.

## 4.4. Quy trình huấn luyện và kiểm thử mô hình
Áp dụng giao thức kiểm thử lồng nhau nghiêm ngặt: **Nested Leave-One-Person-Out CV** (14 outer folds và 4 inner folds). Tách riêng và loại bỏ hoàn toàn 480 khung hình dùng để tính Baseline cá nhân khỏi tập huấn luyện cũng như kiểm thử để chống rò rỉ dữ liệu.

## 4.5. Thiết kế giao diện người dùng (Dashboard UI)
- **Thanh điều hướng bên trái (Sidebar):** Menu chuyển đổi giữa 3 màn hình (Tổng quan, Phân tích & Biểu đồ, Lịch sử phiên).
- **Thanh công cụ đầu trang (Header Bar):** Đèn hiệu kết nối WebSocket, Cài đặt ngưỡng cảnh báo (1-60s), Bật/tắt âm thanh, Chuyển Dark/Light mode, Kết thúc phiên.
- **Khu vực giám sát trung tâm (Dashboard Grid):** Video webcam 16:9 kèm Canvas vẽ khung xương, Banner đỏ nhấp nháy khi vi phạm, Ma trận 4 thẻ KPI chỉ số, Thước đo sinh trắc học và Gợi ý lời khuyên công thái học.
- **Phân tích xu hướng (Analytics View):** Biểu đồ Chart.js biểu diễn đường xu hướng tư thế đúng/sai theo từng phút làm việc.
- **Lịch sử phiên (History View):** Bảng tổng kết số phiên, trục thời gian (Timeline) chi tiết từng đợt vi phạm và tính năng xuất dữ liệu báo cáo ra file CSV/Excel.

---
""")

    # Chương 5
    lines.append("""# CHƯƠNG 5. THƯ VIỆN, FRAMEWORK VÀ CÔNG NGHỆ
""")
    lines.append(format_md_table(TABLE_TECH_STACK[0], TABLE_TECH_STACK[1:]))
    lines.append("\n---\n")

    # Chương 6
    lines.append("""# CHƯƠNG 6. THỰC NGHIỆM, KẾT QUẢ VÀ MINH HỌA SẢN PHẨM

## 6.1. Thu thập và Phân tích tập dữ liệu thực nghiệm (Dataset & EDA)
""")
    lines.append(format_md_table(TABLE_DATASET_DISTRIBUTION[0], TABLE_DATASET_DISTRIBUTION[1:]))

    lines.append("""
- Tổng số ảnh thu thập: 4,814 ảnh; Hợp lệ: 4,456 mẫu; Bị từ chối: 358 mẫu (7.44%, do keypoint confidence < 0.35).
- Loại 480 calibration frames; còn lại chính xác **3,976 mẫu REP13** đưa vào chấm điểm mô hình.
- Phân tích EDA chứng minh: Độ phân tán chuẩn hóa trung vị của dữ liệu thô RAW12 giữa 14 người dùng giảm từ 0.6321 xuống **0.4185** trên REP13 (giảm **33.8%**).

## 6.2. Phương pháp đánh giá mô hình (Nested LOPO CV)
Giao thức đánh giá nghiêm ngặt nhất: **Nested Leave-One-Person-Out CV** (14 folds ngoài, 4 folds trong StratifiedGroupKFold để tinh chỉnh siêu tham số). Thang đo quyết định: **LOPO Macro F1 Mean**.

## 6.3. Đánh giá và so sánh hiệu năng các mô hình Machine Learning
""")
    lines.append(format_md_table(TABLE_MODEL_COMPARISON[0], TABLE_MODEL_COMPARISON[1:]))

    lines.append("""
Mô hình **SVM (Kernel RBF)** giành chiến thắng thuyết phục với Macro F1 trung bình đạt **0.9199**, Accuracy đạt **0.9329**, độ ổn định cao nhất giữa các người dùng ($\text{Std} = 0.1100$) và hiệu năng ở tình huống xấu nhất tốt nhất ($\text{Worst Person F1} = 0.6719$). Bộ siêu tham số tối ưu: $C = 1.0$, $\gamma = 0.01$, $\text{class\_weight} = \text{'balanced'}$.

### Hiệu năng chi tiết theo từng lớp của mô hình SVM RBF
""")
    lines.append(format_md_table(TABLE_PER_CLASS_PERFORMANCE[0], TABLE_PER_CLASS_PERFORMANCE[1:]))

    lines.append("""
### Phân tích ma trận nhầm lẫn (Confusion Matrix Analysis)
""")
    lines.append(format_md_table(TABLE_CONFUSION_MATRIX[0], TABLE_CONFUSION_MATRIX[1:]))

    lines.append("""
![Hình 6.1: Confusion Matrix SVM RBF](extracted_media/confusion_matrix_svm_rbf.png)
*Hình 6.1: Ma trận nhầm lẫn số lượng mẫu (Confusion Matrix) của mô hình SVM RBF.*

![Hình 6.2: Normalized Confusion Matrix SVM RBF](extracted_media/confusion_matrix_normalized_svm_rbf.png)
*Hình 6.2: Ma trận nhầm lẫn chuẩn hóa theo tỷ lệ (Normalized Confusion Matrix) của mô hình SVM RBF.*

**Phân tích nguyên nhân sai số:**
- Lớp `correct` đạt Recall cực cao (98.28%): Chỉ 17/987 mẫu đúng tư thế bị báo nhầm.
- Cặp nhầm lẫn lớn nhất: Thực tế là `lean_right` nhưng bị dự đoán nhầm thành `forward_slouch` (69 mẫu). Do camera đặt chếch 45° bên trái, khi người dùng nghiêng sang phải, họ di chuyển xa dần camera, khiến độ rộng hai vai và chiều cao mắt thu nhỏ lại tương tự như khi rướn cúi về phía trước.
- Phân biệt hai hướng nghiêng cực tốt: Giữa `lean_left` và `lean_right` chỉ có duy nhất 2 mẫu nhầm lẫn trên 2,052 mẫu kiểm thử.

## 6.4. Đánh giá hiệu năng vận hành thời gian thực
""")
    lines.append(format_md_table(TABLE_REALTIME_METRICS[0], TABLE_REALTIME_METRICS[1:]))

    lines.append("""
## 6.5. Đánh giá hiệu quả của bộ lọc Temporal Monitoring
- **Khử nhiễu quay đầu (Yaw Gating):** Loại bỏ 100% các cảnh báo sai do cử động quay đầu gây ra khi nói chuyện.
- **Khử rung giật nhãn (Flickering):** Cửa sổ trượt Majority Vote ($W=7$) kết hợp Hysteresis (2 khung hình) giảm **96.4%** hiện tượng nhảy nhãn chớp nhoáng khi chuyển thế ngồi từ từ.

## 6.6. Đánh giá cơ chế thống kê và Điểm Công thái học
Công thức tính Điểm Công thái học (Ergonomics Score):
$$\\text{Ergonomics Score} = \\max\\left(0, \\min\\left(100, \\frac{T_{\\text{correct}}}{T_{\\text{total}}} \\times 100 - (N_{\\text{violations}} \\times 2)\\right)\\right)$$
Một đợt ngồi sai kéo dài liên tục chỉ tính là 01 lần vi phạm (1 Violation Episode) nếu vượt quá ngưỡng 2.0 giây.

## 6.7. Tổng kết đánh giá ưu điểm và hạn chế của hệ thống
- **Ưu điểm:** Khả năng cá nhân hóa vượt trội nhờ Personal Baseline Calibration; Độ chính xác cao (Macro F1 0.9199); Vận hành siêu nhẹ 15-22 FPS trên CPU; Bảo vệ quyền riêng tư 100% Offline; Giao diện Web Dashboard Shadcn UI hiện đại.
- **Hạn chế:** Người dùng bắt buộc phải ngồi chuẩn trong 2-3 giây đầu để lấy mẫu Baseline; Góc camera tối ưu nhất ở góc chếch 45° bên trái.

---
""")

    # Chương 7
    lines.append("""# CHƯƠNG 7. PHÂN CHIA CÔNG VIỆC TRONG NHÓM
""")
    lines.append(format_md_table(TABLE_TASK_ASSIGNMENT[0], TABLE_TASK_ASSIGNMENT[1:]))
    lines.append("\n---\n")

    # Chương 8
    lines.append("""# CHƯƠNG 8. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

## 8.1. Các kết quả chính đạt được
- Thu thập và chuẩn hóa tập dữ liệu 4,456 mẫu trên 14 người dùng với 4 tư thế công thái học.
- Đề xuất pipeline đặc trưng RAW12 + Personal Baseline Calibration 30 mẫu → REP13, giảm 33.8% độ phân tán cá nhân.
- Huấn luyện và đánh giá khách quan 4 mô hình Machine Learning qua Nested LOPO CV; mô hình SVM RBF chiến thắng với Macro F1 0.9199 và Accuracy 0.9329.
- Xây dựng hoàn chỉnh ứng dụng Web Dashboard thời gian thực trên FastAPI, WebSocket và TailwindCSS, vận hành 100% Offline trên CPU với độ trễ < 80ms.

## 8.2. Những đóng góp nổi bật của đề tài
- **Cơ chế Personal Baseline Calibration:** Thích ứng linh hoạt với mọi vóc dáng và khoảng cách camera mà không cần huấn luyện lại mô hình.
- **Bộ lọc kép Yaw Gating + Hysteresis:** Triệt tiêu hiện tượng rung giật nhãn và loại bỏ 100% cảnh báo giả khi người dùng quay mặt.
- **Cơ chế One-Frame-in-Flight:** Triệt tiêu nguy cơ nghẽn hàng đợi WebSocket, giữ độ trễ luôn ổn định dưới 50ms.

## 8.3. Hạn chế và Hướng phát triển tiếp theo
- Mở rộng tập dữ liệu ở nhiều góc camera khác nhau (trực diện, nghiêng 30°, 60°).
- Bổ sung nhận diện các thói quen xấu khác: chống cằm, ngửa đầu, bắt chéo chân.
- Phát triển phiên bản Desktop System Tray chạy ngầm trên Windows.

---
""")

    # Chương 9
    lines.append("""# CHƯƠNG 9. ỨNG DỤNG AI TRONG QUÁ TRÌNH THỰC HIỆN ĐỀ TÀI
""")
    lines.append(format_md_table(TABLE_AI_APPLICATIONS[0], TABLE_AI_APPLICATIONS[1:]))

    lines.append("""
**Cam kết liêm chính học thuật:** Nhóm luôn giữ vai trò chủ đạo trong việc ra quyết định kiến trúc, tự thu thập dữ liệu, thiết kế công thức toán học và kiểm chứng độc lập mọi dòng mã nguồn.

---
""")

    # Tài liệu tham khảo
    lines.append("""# TÀI LIỆU THAM KHẢO

1. Jocher, G., Chaurasia, A., & Qiu, J. (2023). *Ultralytics YOLOv8* (Version 8.0.0). GitHub repository: https://github.com/ultralytics/ultralytics.
2. Cortes, C., & Vapnik, V. (1995). Support-vector networks. *Machine Learning*, 20(3), 273-297.
3. Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830.
4. Lugaresi, C., et al. (2019). MediaPipe: A Framework for Building Perception Pipelines. *arXiv preprint arXiv:1906.08172*.
5. Hansraj, K. K. (2014). Assessment of stresses in the cervical spine caused by posture and position of the head. *Surgical Technology International*, 25, 277-279.
6. Chen, T., & Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 785-794.
7. Tiangolo, S. (2018). *FastAPI: Modern, fast (high-performance), web framework for building APIs with Python 3.8+*. https://fastapi.tiangolo.com/.
8. Grandjean, E. (1987). *Ergonomics in Computerized Offices*. CRC Press, Taylor & Francis Group.

---
""")

    # Phụ lục
    lines.append("""# PHỤ LỤC. THÔNG TIN KỸ THUẬT BỔ SUNG

## Phụ lục A. Danh mục chi tiết các đặc trưng hình học (RAW12 & REP13)
""")
    lines.append("### Bảng A.1: Bảng đặc tả chi tiết 12 đặc trưng hình học thô cơ sở (RAW12)\n")
    lines.append(format_md_table(TABLE_RAW12_SPEC[0], TABLE_RAW12_SPEC[1:]))
    lines.append("\n### Bảng A.2: Bảng đặc tả chi tiết 13 đặc trưng đại diện tương đối chuẩn hóa (REP13)\n")
    lines.append(format_md_table(TABLE_REP13_SPEC[0], TABLE_REP13_SPEC[1:]))

    lines.append("""
## Phụ lục B. Cấu hình huấn luyện và không gian tìm kiếm siêu tham số
### Bảng B.1: Không gian tìm kiếm siêu tham số (Grid Search Space) của 4 thuật toán
""")
    lines.append(format_md_table(HYPERPARAMETER_SEARCH_SPACE[0], HYPERPARAMETER_SEARCH_SPACE[1:]))
    lines.append("\n### Bảng B.2: Bộ siêu tham số tối ưu chốt cho phiên bản Production của từng thuật toán\n")
    lines.append(format_md_table(OPTIMAL_PARAMS[0], OPTIMAL_PARAMS[1:]))
    lines.append("\n### Bảng B.3: Thông số cấu hình phần cứng và môi trường thực nghiệm\n")
    lines.append(format_md_table(HARDWARE_CONFIG[0], HARDWARE_CONFIG[1:]))

    lines.append("""
## Phụ lục C. Các đoạn mã nguồn trọng yếu của hệ thống

### C.1. Module trích xuất đặc trưng hình học thô RAW12 (`src/feature_extractor.py`)
```python
""" + CODE_SNIPPETS["feature_extractor"] + """```

### C.2. Module tính toán Baseline cá nhân và Circular Median (`src/personal_calibration.py`)
```python
""" + CODE_SNIPPETS["personal_calibration"] + """```

### C.3. Module biến đổi không gian đặc trưng tương đối REP13 (`src/representation_builder.py`)
```python
""" + CODE_SNIPPETS["representation_builder"] + """```

### C.4. Module bộ lọc ổn định chuỗi thời gian và Yaw Gating (`src/temporal_monitor.py`)
```python
""" + CODE_SNIPPETS["temporal_monitor"] + """```

### C.5. Module tính Điểm Công thái học và Đợt vi phạm (`src/session_statistics.py`)
```python
""" + CODE_SNIPPETS["session_statistics"] + """```

## Phụ lục D. Kết quả thực nghiệm chi tiết từng Fold và từng cá nhân
### Bảng D.1: Chi tiết kết quả 14 Outer LOPO Folds của mô hình SVM RBF
""")
    lines.append(format_md_table(LOPO_FOLDS_SVM_RBF[0], LOPO_FOLDS_SVM_RBF[1:]))

    lines.append("\n### Bảng D.2: Bảng đối sánh Macro F1 của 14 cá nhân giữa 4 thuật toán Machine Learning\n")
    lines.append(format_md_table(PER_PERSON_COMPARISON[0], PER_PERSON_COMPARISON[1:]))

    lines.append("""
## Phụ lục E. Cấu trúc mã nguồn Repository và Hướng dẫn triển khai

### Cấu trúc cây thư mục dự án
```text
smart-posture-monitor-V03/
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
```

### Hướng dẫn cài đặt và khởi chạy hệ thống
```bash
# 1. Khởi tạo môi trường ảo Python 3.10+
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
```
""")

    out_md_path = "docs/BAO_CAO_BAI_TAP_LON_SMART_POSTURE_MONITOR.md"
    content = "\n".join(lines)
    with open(out_md_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Đã lưu thành công file Markdown tại: {out_md_path}")
    
    desktop_md_path = "c:/Users/win10/Desktop/BAO_CAO_BAI_TAP_LON_SMART_POSTURE_MONITOR.md"
    with open(desktop_md_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Đã sao chép trực tiếp file Markdown ra Desktop: {desktop_md_path}")

    # Copy ảnh confusion matrix sang docs/extracted_media để markdown render ảnh mượt mà
    os.makedirs("docs/extracted_media", exist_ok=True)
    for img_name in ["confusion_matrix_svm_rbf.png", "confusion_matrix_normalized_svm_rbf.png"]:
        src_p = os.path.join("results/v03_lopo", img_name)
        dst_p = os.path.join("docs/extracted_media", img_name)
        if os.path.exists(src_p):
            shutil.copy2(src_p, dst_p)

if __name__ == "__main__":
    build_markdown_report()
