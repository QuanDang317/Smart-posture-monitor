"""
Module: report_data.py
Chứa toàn bộ nội dung, dữ liệu bảng, thông số kỹ thuật và mã nguồn minh họa
cho Báo cáo Bài tập lớn: "Hệ thống giám sát tư thế ngồi thời gian thực (Smart Posture Monitor)"
"""

METADATA = {
    "institution": "HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG",
    "faculty": "KHOA CÔNG NGHỆ THÔNG TIN 1",
    "department": "BỘ MÔN LẬP TRÌNH PYTHON",
    "report_type": "BÁO CÁO BÀI TẬP LỚN",
    "course_name": "Lập trình Python",
    "project_title": "XÂY DỰNG HỆ THỐNG GIÁM SÁT TƯ THẾ NGỒI THỜI GIAN THỰC",
    "project_subtitle": "SMART POSTURE MONITOR (V03)",
    "instructor": "ThS. Phạm Danh Tuyên",
    "students": [
        {"name": "Dương Ngọc Quang", "code": "B24DCKH112", "role": "Nhóm trưởng"},
        {"name": "Đặng Xuân Quân", "code": "B24DCKH105", "role": "Thành viên"},
        {"name": "Hoàng Hữu Mạnh", "code": "B24DCKH080", "role": "Thành viên"}
    ],
    "class_name": "D24CQKH01-B",
    "location": "Hà Nội",
    "date": "Tháng 10 năm 2026"
}

GLOSSARY = [
    ("RAW12", "Vector 12 đặc trưng hình học cơ sở trích xuất trực tiếp từ 6 điểm keypoint vùng đầu và vai trên ảnh 2D."),
    ("REP13", "Vector 13 đặc trưng đại diện tương đối, được chuẩn hóa từ RAW12 thông qua mốc tham chiếu Baseline cá nhân."),
    ("Baseline", "Vector mốc tham chiếu tư thế ngồi chuẩn công thái học của từng người dùng, thu thập từ 30 khung hình hợp lệ."),
    ("LOPO CV", "Leave-One-Person-Out Cross-Validation: Giao thức kiểm thử chéo loại trừ từng cá nhân độc lập nhằm đánh giá khả năng tổng quát hóa trên người dùng mới."),
    ("OOF", "Out-of-Fold: Tập hợp các dự đoán độc lập trên tập kiểm thử ngoài trong toàn bộ các lượt chia fold."),
    ("Macro-F1", "Điểm F1 trung bình cộng không trọng số giữa các lớp; đánh giá công bằng hiệu năng phân loại trên tập dữ liệu mất cân bằng."),
    ("Weighted-F1", "Điểm F1 trung bình có tính đến trọng số tỷ lệ mẫu của từng lớp tư thế."),
    ("YOLO-Pose", "Kiến trúc mạng nơ-ron tích chập thời gian thực (You Only Look Once) chuyên biệt cho tác vụ ước lượng dáng người và định vị khớp xương."),
    ("Keypoints", "Các điểm mốc giải phẫu trên cơ thể người (khớp xương, ngũ quan) được mô hình thị giác định vị tọa độ và độ tin cậy."),
    ("SVM (Kernel RBF)", "Support Vector Machine với nhân Radial Basis Function: Thuật toán học máy phân tách siêu phẳng phi tuyến trong không gian đặc trưng nhiều chiều."),
    ("Circular Median", "Thuật toán xác định trung vị góc có xử lý tính chất tuần hoàn trên đường tròn nhằm triệt tiêu sai số đứt gãy tại chu kỳ ±180°."),
    ("Temporal Smoothing", "Kỹ thuật làm mượt chuỗi thời gian dựa trên cửa sổ trượt bầu chọn đa số (Majority Vote) để loại bỏ nhiễu rung giật nhãn đơn lẻ."),
    ("Hysteresis", "Cơ chế trễ chuyển đổi trạng thái: Yêu cầu trạng thái mới duy trì tối thiểu N khung hình liên tiếp trước khi chính thức chuyển đổi nhãn hiển thị."),
    ("Yaw Gating", "Bộ lọc kiểm soát góc xoay mặt: Sử dụng tỷ lệ khoảng cách mắt - mũi để phát hiện hành vi quay đầu, tự động khóa trạng thái thân trên nhằm chống báo động sai."),
    ("Ergonomics Score", "Điểm số công thái học đánh giá chất lượng phiên ngồi theo thang điểm 100 dựa trên tỷ lệ thời gian ngồi đúng và số lần vi phạm."),
    ("WebSocket", "Giao thức truyền thông hai chiều độ trễ thấp qua một kết nối TCP duy nhất, cho phép truyền nhận luồng video và kết quả AI liên tục giữa Client và Server.")
]

TABLE_COMPARISON_APPROACHES = [
    ["Tiêu chí so sánh", "Quy tắc hình học (Rule-based)", "Học sâu trực tiếp (End-to-End DL)", "Pose Estimation + Feature + ML (Đề xuất)"],
    ["Dữ liệu huấn luyện bộ phân loại", "Không yêu cầu (dựa trên ngưỡng cứng)", "Rất lớn và đa dạng hình ảnh", "Vừa phải (tập trung vào vector đặc trưng hình học)"],
    ["Độ phức tạp tính toán suy luận", "Rất thấp", "Rất cao (xử lý toàn bộ pixel trên GPU)", "Thấp đến trung bình (chạy mượt trên CPU máy tính văn phòng)"],
    ["Khả năng giải thích (Interpretability)", "Rất cao (ngưỡng góc tường minh)", "Hộp đen (Black-box), khó chẩn đoán lỗi", "Rất cao (đặc trưng góc, khoảng cách, độ lệch tương đối rõ ràng)"],
    ["Khả năng thích ứng theo cá nhân", "Rất kém (ngưỡng cứng sai lệch theo thể trạng)", "Khó can thiệp cá nhân hóa nhanh", "Rất tốt (tích hợp Personal Baseline Calibration 30 mẫu)"],
    ["Độ bền vững trước nhiễu ngoại cảnh", "Kém (nhạy với góc camera và rung động)", "Phụ thuộc vào ánh sáng và bối cảnh phòng", "Rất tốt (Pose model lọc nhiễu nền; đặc trưng chuẩn hóa theo vai)"]
]

TABLE_VERSION_EVOLUTION = [
    ["Tiêu chí kỹ thuật", "Phiên bản V01 (Baseline)", "Phiên bản V02 (Mở rộng)", "Phiên bản V03 (Hoàn thiện - Đề xuất)"],
    ["Hướng tiếp cận", "Pose 17 kps + 18 đặc trưng tuyệt đối + ML", "Pose 17 kps + 29 đặc trưng góc/khoảng cách + ML", "Pose 6 kps + RAW12 + Personal Calibration + REP13 + SVM"],
    ["Số lượng keypoint sử dụng", "17 keypoint toàn thân (nhiều điểm thừa)", "17 keypoint toàn thân", "6 keypoint vùng đầu - vai (Mũi, 2 Mắt, Tai trái, 2 Vai)"],
    ["Cơ chế cá nhân hóa", "Không có", "Không có", "Personal Calibration (30 mẫu correct, Circular Median)"],
    ["Không gian đặc trưng", "18 đặc trưng pixel thô tuyệt đối", "29 đặc trưng hình học tuyệt đối", "RAW12 (Hình học thô) → REP13 (Độ lệch tương đối & Tỷ lệ)"],
    ["Xử lý chuỗi thời gian", "Không có (dự đoán từng frame riêng rẽ)", "Bộ lọc trung bình trượt đơn giản", "Temporal Smoothing (Majority Vote W=7) + Hysteresis + Yaw Gating"],
    ["Giao thức kiểm thử", "K-Fold ngẫu nhiên (Rò rỉ chủ thể)", "Group K-Fold", "Nested Leave-One-Person-Out CV (14 folds ngoài, 4 folds trong)"],
    ["Độ chính xác Macro F1", "0.782", "0.846", "0.9199 (LOPO F1) / 0.9363 (OOF F1)"],
    ["Mục tiêu trọng tâm", "Kiểm chứng tính khả thi", "Tối ưu hóa số lượng đặc trưng", "Cá nhân hóa, chống rung giật thời gian thực và ứng dụng web"]
]

TABLE_KEYPOINTS = [
    ["STT", "Tên Keypoint (COCO)", "Chỉ số Index", "Tọa độ trích xuất", "Vai trò và Ý nghĩa sinh trắc học trong hệ thống"],
    ["1", "Nose (Mũi)", "0", "(x_0, y_0, conf_0)", "Mốc trung tâm khuôn mặt; kết hợp tai trái xác định hướng cúi đầu (neck pitch) và tỷ lệ quay mặt (yaw proxy)."],
    ["2", "Left Eye (Mắt trái)", "1", "(x_1, y_1, conf_1)", "Kết hợp mắt phải xác định trục nghiêng đầu (eye roll), tâm mắt và khoảng cách gian đồng tử."],
    ["3", "Right Eye (Mắt phải)", "2", "(x_2, y_2, conf_2)", "Cùng mắt trái xác định đường cơ sở khuôn mặt và độ lệch ngang/dọc giữa đầu và thân mình."],
    ["4", "Left Ear (Tai trái)", "3", "(x_3, y_3, conf_3)", "Điểm mốc bên hông đầu quan sát rõ nhất từ góc camera 45° bên trái; tính góc gập cổ (neck flexion)."],
    ["5", "Left Shoulder (Vai trái)", "5", "(x_5, y_5, conf_5)", "Kết hợp vai phải xác định trục nghiêng thân trên (shoulder roll), tâm vai và độ rộng vai cơ sở."],
    ["6", "Right Shoulder (Vai phải)", "6", "(x_6, y_6, conf_6)", "Cùng vai trái xác định đường vai; dùng làm mẫu số chuẩn hóa độ rộng vai (W_0) cho mọi khoảng cách."]
]

TABLE_RAW12_SPEC = [
    ["Mã", "Tên đặc trưng", "Nhóm đặc trưng", "Công thức toán học", "Đơn vị", "Mô tả ý nghĩa hình học"],
    ["RAW01", "shoulder_roll_deg", "Hướng (Orientation)", "atan2(y_rs - y_ls, x_rs - x_ls) * 180 / π", "Độ (°)", "Góc nghiêng của đường nối hai vai so với trục hoành ảnh."],
    ["RAW02", "eye_roll_deg", "Hướng (Orientation)", "atan2(y_re - y_le, x_re - x_le) * 180 / π", "Độ (°)", "Góc nghiêng của đường nối hai mắt so với trục hoành ảnh."],
    ["RAW03", "head_shoulder_roll_diff_deg", "Hướng (Orientation)", "wrap(eye_roll_deg - shoulder_roll_deg)", "Độ (°)", "Độ lệch góc giữa trục đầu và trục vai (nhận diện vẹo cổ độc lập với vai)."],
    ["RAW04", "neck_pitch_deg", "Mặt đứng dọc (Sagittal)", "atan2(y_nose - y_lear, x_nose - x_lear) * 180 / π", "Độ (°)", "Góc nghiêng của đoạn nối tai trái - mũi; phản ánh mức độ cúi/ngẩng đầu ở góc 45°."],
    ["RAW05", "eye_center_x_px", "Không gian (Spatial)", "(x_le + x_re) / 2", "Pixel", "Tọa độ hoành độ trung tâm vùng mắt (đại diện vị trí đầu)."],
    ["RAW06", "eye_center_y_px", "Không gian (Spatial)", "(y_le + y_re) / 2", "Pixel", "Tọa độ tung độ trung tâm vùng mắt (phát hiện đầu sụt xuống khi gù)."],
    ["RAW07", "shoulder_center_x_px", "Không gian (Spatial)", "(x_ls + x_rs) / 2", "Pixel", "Tọa độ hoành độ trung tâm hai vai (đại diện vị trí thân trên)."],
    ["RAW08", "eye_shoulder_vertical_gap_px", "Không gian (Spatial)", "y_shoulder_center - y_eye_center", "Pixel", "Khoảng cách thẳng đứng từ tâm mắt đến tâm vai (thu nhỏ khi rướn/gù)."],
    ["RAW09", "eye_shoulder_horizontal_offset_px", "Không gian (Spatial)", "x_eye_center - x_shoulder_center", "Pixel", "Độ lệch ngang có dấu giữa tâm mắt và tâm vai (phát hiện lệch trục đầu/thân)."],
    ["RAW10", "inter_eye_distance_px", "Phối cảnh & Tỷ lệ", "sqrt((x_re - x_le)^2 + (y_re - y_le)^2)", "Pixel", "Khoảng cách Euclidean hai mắt; thay đổi theo cự ly người đến camera."],
    ["RAW11", "ear_nose_horizontal_span_px", "Phối cảnh & Tỷ lệ", "|x_nose - x_lear|", "Pixel", "Độ chênh lệch hoành độ tai-mũi; nhạy với góc quay mặt (yaw) và rướn cổ."],
    ["RAW12", "shoulder_width_px", "Phối cảnh & Tỷ lệ", "sqrt((x_rs - x_ls)^2 + (y_rs - y_ls)^2)", "Pixel", "Khoảng cách Euclidean hai vai; dùng làm thước đo chuẩn hóa cơ thể."]
]

TABLE_REP13_SPEC = [
    ["Mã", "Tên đặc trưng", "Nguồn gốc RAW", "Công thức biến đổi từ Baseline cá nhân", "Miền giá trị", "Ý nghĩa phân lớp"],
    ["REP01", "delta_shoulder_roll_deg", "RAW01", "wrap(RAW01 - Baseline[0])", "[-180°, 180°)", "Độ lệch nghiêng vai so với tư thế chuẩn (phân biệt lean_left / lean_right)."],
    ["REP02", "delta_eye_roll_deg", "RAW02", "wrap(RAW02 - Baseline[1])", "[-180°, 180°)", "Độ lệch nghiêng đầu so với tư thế chuẩn."],
    ["REP03", "delta_head_shoulder_roll_diff_deg", "RAW03", "wrap(RAW03 - Baseline[2])", "[-180°, 180°)", "Biến thiên mức độ vặn lệch giữa đầu và vai."],
    ["REP04", "delta_neck_pitch_deg", "RAW04", "wrap(RAW04 - Baseline[3])", "[-180°, 180°)", "Biến thiên góc gập cổ (chỉ số chính nhận diện forward_slouch)."],
    ["REP05", "delta_eye_center_x_body", "RAW05", "(RAW05 - Baseline[4]) / W_0", "(-∞, +∞)", "Độ dịch ngang của đầu chuẩn hóa theo độ rộng vai."],
    ["REP06", "delta_eye_center_y_body", "RAW06", "(RAW06 - Baseline[5]) / W_0", "(-∞, +∞)", "Độ sụt dọc của đầu chuẩn hóa theo độ rộng vai (gap = 1.387 cho forward_slouch)."],
    ["REP07", "delta_shoulder_center_x_body", "RAW07", "(RAW07 - Baseline[6]) / W_0", "(-∞, +∞)", "Độ dịch ngang thân mình chuẩn hóa (phân tách mạnh giữa lean_left và lean_right)."],
    ["REP08", "delta_eye_shoulder_vertical_gap_body", "RAW08", "(RAW08 - Baseline[7]) / W_0", "(-∞, +∞)", "Độ co ngắn khoảng cách đầu-vai chuẩn hóa theo vai."],
    ["REP09", "delta_eye_shoulder_horizontal_offset_body", "RAW09", "(RAW09 - Baseline[8]) / W_0", "(-∞, +∞)", "Độ lệch tâm đầu-vai tương đối chuẩn hóa."],
    ["REP10", "log_ratio_inter_eye_distance", "RAW10", "ln(RAW10 / Baseline[9])", "(-∞, +∞)", "Tỷ số log khoảng cách mắt; >0 khi tiến sát camera, <0 khi lùi xa."],
    ["REP11", "log_ratio_ear_nose_horizontal_span", "RAW11", "ln(RAW11 / Baseline[10])", "(-∞, +∞)", "Tỷ số log độ rộng tai-mũi; biến thiên khi rướn về trước."],
    ["REP12", "log_ratio_shoulder_width", "RAW12", "ln(RAW12 / Baseline[11])", "(-∞, +∞)", "Tỷ số log độ rộng hai vai; phản ánh góc nghiêng thân và phối cảnh."],
    ["REP13", "head_drift_magnitude", "REP05, REP06", "sqrt((REP05)^2 + (REP06)^2)", "[0, +∞)", "Độ lớn dịch chuyển tổng hợp của đầu (gap = 1.961 phân biệt correct và lean)."]
]

TABLE_MODEL_ALGORITHMS = [
    ["Tiêu chí", "SVM (Kernel RBF)", "Random Forest", "XGBoost", "Đa tầng nơ-ron (MLP)"],
    ["Bản chất toán học", "Phân tách siêu phẳng phi tuyến lề cực đại qua không gian Hilbert", "Tổ hợp biểu quyết của nhiều cây quyết định độc lập (Bagging)", "Tối ưu hóa hàm mất mát bằng chuỗi cây quyết định tuần tự (Gradient Boosting)", "Mạng nơ-ron truyền thẳng học biểu diễn qua các hàm kích hoạt phi tuyến"],
    ["Xử lý quan hệ phi tuyến", "Xuất sắc (nhân RBF tự động biến đổi sang không gian vô hạn chiều)", "Tốt (chia cắt trực giao từng thuộc tính)", "Rất tốt (học tương tác phức tạp)", "Xuất sắc (các tầng ẩn phi tuyến)"],
    ["Độ nhạy với chuẩn hóa dữ liệu", "Rất nhạy (đòi hỏi đặc trưng cùng thang đo)", "Không nhạy với thang đo", "Không nhạy với thang đo", "Rất nhạy (cần chuẩn hóa và điều chuẩn trọng số)"],
    ["Khả năng tổng quát hóa với dữ liệu ít", "Rất cao (kháng overfitting tốt nhờ tối ưu lề cực đại)", "Trung bình (dễ overfit trên tập dữ liệu nhỏ)", "Trung bình (cần tinh chỉnh nhiều tham số)", "Kém trên tập dữ liệu nhỏ (dễ overfit hoặc bất ổn định)"],
    ["Thời gian suy luận thời gian thực", "< 0.5 ms / mẫu (rất nhẹ khi số vector hỗ trợ vừa phải)", "~ 2 - 5 ms / mẫu (tùy số lượng cây)", "~ 1 - 3 ms / mẫu", "~ 0.5 - 1 ms / mẫu"],
    ["Bộ siêu tham số chính", "C, gamma, class_weight", "n_estimators, max_depth, min_samples_split", "n_estimators, learning_rate, max_depth, reg_lambda", "hidden_layer_sizes, alpha, learning_rate_init"]
]

TABLE_MODULES = [
    ["Module", "File cài đặt", "Chức năng chính", "Đầu vào", "Đầu ra"],
    ["PoseDetector", "src/pose_detector.py", "Phát hiện người trung tâm và trích xuất 6 keypoints vùng đầu-vai bằng YOLOv8-Pose Nano.", "Ảnh RGB (np.ndarray 640x480)", "Tọa độ 6 keypoint (x, y, conf)"],
    ["FeatureExtractor", "src/feature_extractor.py", "Kiểm tra tính hợp lệ hình học và tính toán 12 đặc trưng hình học thô (RAW12).", "Tọa độ 6 keypoint", "Vector RAW12 (12 float32)"],
    ["PersonalCalibration", "src/personal_calibration.py", "Thu thập 30 mẫu correct hợp lệ và tính vector Baseline bằng Circular Median và Median.", "Chuỗi mẫu RAW12 correct", "Vector Baseline cá nhân (12 float32)"],
    ["RepresentationBuilder", "src/representation_builder.py", "Biến đổi vector RAW12 và Baseline thành vector đại diện tương đối 13 chiều (REP13).", "RAW12 hiện tại + Baseline", "Vector REP13 (13 float32)"],
    ["PosturePredictor", "src/posture_predictor.py", "Nạp mô hình SVM RBF đã huấn luyện và dự đoán xác suất, nhãn tư thế tức thời.", "Vector REP13", "Nhãn thô và phân bố xác suất"],
    ["TemporalMonitor", "src/temporal_monitor.py", "Ổn định chuỗi thời gian bằng Yaw Gating, Sliding Window Majority Vote và Hysteresis.", "Nhãn thô + tỷ lệ quay mặt", "Nhãn tư thế ổn định tuyệt đối"],
    ["SessionStatistics", "src/session_statistics.py", "Đo thời gian thực, đếm số đợt vi phạm và tính Điểm Công thái học phiên làm việc.", "Nhãn ổn định theo chu kỳ thời gian", "KPI phiên (Thời gian, Số lỗi, Điểm số)"],
    ["WebApplication / API", "app/app.py & static/index.html", "Máy chủ ASGI FastAPI kết nối WebSocket hai chiều, cung cấp Dashboard Shadcn UI.", "Luồng frame từ trình duyệt", "JSON kết quả AI + Skeleton Canvas"]
]

TABLE_TECH_STACK = [
    ["Công nghệ / Thư viện", "Phiên bản", "Vai trò trong hệ thống", "Lý do lựa chọn sử dụng"],
    ["Python", "3.10+", "Ngôn ngữ lập trình chính", "Ngôn ngữ tiêu chuẩn trong AI/CV với hệ sinh thái thư viện phong phú, đồng bộ và hiệu năng tính toán cao."],
    ["OpenCV (opencv-python)", "≥ 4.8.0", "Xử lý ảnh và luồng Camera", "Giải mã luồng ảnh Base64 từ WebSocket, xử lý mảng pixel, vẽ khung xương tọa độ cực nhanh và tối ưu bộ nhớ."],
    ["Ultralytics YOLOv8 (yolo26n-pose.pt)", "≥ 8.0.0", "Ước lượng dáng người (Pose Estimation)", "Mô hình Nano siêu nhẹ (~6MB), tốc độ suy luận 15-30ms trên CPU văn phòng, độ tin cậy vượt trội trên 17 điểm khớp."],
    ["NumPy", "≥ 1.24.0", "Xử lý tính toán ma trận, vector", "Tính toán khoảng cách Euclidean, tích vô hướng, hàm lượng giác và thuật toán Circular Median với tốc độ vector hóa."],
    ["Pandas", "≥ 2.0.0", "Quản trị dữ liệu thực nghiệm", "Xử lý, làm sạch và lưu trữ tập dữ liệu trích xuất đặc trưng (features.csv), phục vụ phân tích EDA và huấn luyện mô hình."],
    ["scikit-learn", "≥ 1.3.0", "Xây dựng pipeline ML & Đánh giá", "Huấn luyện thuật toán SVM RBF, thiết lập Nested LOPO CV, tính ma trận nhầm lẫn và các thang đo Precision, Recall, F1."],
    ["XGBoost", "≥ 2.0.0", "Mô hình phân loại đối sánh", "Thuật toán Gradient Boosting trên cây quyết định phục vụ nghiên cứu đối sánh hiệu năng với SVM trên dữ liệu bảng."],
    ["Joblib", "≥ 1.3.0", "Đóng gói mô hình (Serialization)", "Lưu trữ và nạp tức thì trọng số mô hình đã huấn luyện (best_model.joblib) lên bộ nhớ RAM của server."],
    ["FastAPI & Uvicorn", "0.100+ / 0.20+", "Web Backend & ASGI Server", "Framework bất đồng bộ hiện đại, hiệu năng cao vượt trội so với Flask, hỗ trợ giao thức WebSocket hai chiều ổn định."],
    ["WebSocket (Chuẩn W3C)", "RFC 6455", "Truyền dẫn dữ liệu thời gian thực", "Truyền liên tục khung hình từ client lên server và nhận kết quả dự đoán với độ trễ < 50ms, triệt tiêu overhead HTTP."],
    ["HTML5, TailwindCSS, Lucide", "CDN / Offline", "Giao diện người dùng (Dashboard UI)", "Thiết kế Dashboard phong cách Shadcn UI hiện đại, trực quan, hỗ trợ Dark/Light mode và tương thích mọi kích thước màn hình."],
    ["Chart.js", "4.x", "Trực quan hóa dữ liệu thống kê", "Thư viện vẽ biểu đồ Canvas nhẹ, mượt; hiển thị biểu đồ tròn và đường xu hướng tư thế ngồi theo thời gian."],
    ["Pytest", "≥ 7.0.0", "Kiểm thử tự động (Unit Testing)", "Chạy tự động bộ 8 file kiểm thử chất lượng mã nguồn từ khâu trích xuất đặc trưng đến độ trễ và luồng WebSocket."],
    ["Git & GitHub", "Latest", "Quản lý phiên bản mã nguồn", "Quản lý lịch sử phát triển phần mềm, làm việc nhóm và bảo đảm tính tái lập của kết quả nghiên cứu."]
]

TABLE_DATASET_DISTRIBUTION = [
    ["Lớp tư thế (Label)", "Ý nghĩa tư thế công thái học", "Số mẫu thô ban đầu", "Mẫu dùng Calibration", "Mẫu đưa vào đánh giá (REP13)", "Tỷ lệ (%)"],
    ["correct", "Ngồi thẳng lưng, chuẩn công thái học", "1,467", "480", "987", "24.82%"],
    ["forward_slouch", "Cúi đầu, rướn cổ, gù lưng về phía trước", "937", "0", "937", "23.57%"],
    ["lean_left", "Nghiêng đầu và vẹo thân sang bên trái", "1,024", "0", "1,024", "25.75%"],
    ["lean_right", "Nghiêng đầu và vẹo thân sang bên phải", "1,028", "0", "1,028", "25.86%"],
    ["Tổng cộng", "Tập dữ liệu hoàn chỉnh 14 đối tượng", "4,456", "480", "3,976", "100.0%"]
]

TABLE_MODEL_COMPARISON = [
    ["Thứ hạng", "Mô hình (Model)", "LOPO Macro F1 Mean", "Độ lệch chuẩn (Std)", "Worst Person F1", "Accuracy Mean", "F1 lớp Correct", "Thời gian huấn luyện (s)"],
    ["1", "SVM (Kernel RBF)", "0.9199", "0.1100", "0.6719", "0.9329", "0.9381", "300.75"],
    ["2", "Random Forest", "0.8993", "0.1375", "0.6444", "0.9159", "0.9143", "789.70"],
    ["3", "Đa tầng nơ-ron (MLP)", "0.8991", "0.1240", "0.6187", "0.9171", "0.9400", "108.51"],
    ["4", "XGBoost", "0.8736", "0.1465", "0.6315", "0.8947", "0.9099", "368.39"]
]

TABLE_PER_CLASS_PERFORMANCE = [
    ["Lớp tư thế (Class)", "Precision", "Recall", "F1-Score", "Số lượng mẫu (Support)"],
    ["correct (Ngồi chuẩn)", "0.8973", "0.9828", "0.9381", "987"],
    ["forward_slouch (Gù lưng / cúi)", "0.8960", "0.9200", "0.9078", "937"],
    ["lean_left (Nghiêng trái)", "0.9841", "0.9648", "0.9744", "1,024"],
    ["lean_right (Nghiêng phải)", "0.9742", "0.8804", "0.9249", "1,028"],
    ["Bình quân Macro (Macro Avg)", "0.9379", "0.9370", "0.9363", "3,976"],
    ["Bình quân gia quyền (Weighted Avg)", "0.9380", "0.9369", "0.9369", "3,976"]
]

TABLE_CONFUSION_MATRIX = [
    ["Thực tế \\ Dự đoán", "correct", "forward_slouch", "lean_left", "lean_right", "Tổng thực tế"],
    ["correct", "970", "6", "5", "6", "987"],
    ["forward_slouch", "48", "862", "9", "18", "937"],
    ["lean_left", "11", "25", "988", "0", "1,024"],
    ["lean_right", "52", "69", "2", "905", "1,028"],
    ["Tổng dự đoán", "1,081", "962", "1,004", "929", "3,976"]
]

TABLE_REALTIME_METRICS = [
    ["Chỉ số kỹ thuật", "Giá trị thực nghiệm đạt được", "Tiêu chuẩn đặt ra ban đầu", "Đánh giá chất lượng thực tế"],
    ["Tốc độ xử lý khung hình (Frame Rate)", "15 – 22 FPS", "≥ 15 FPS", "Đạt chuẩn thời gian thực mượt mà."],
    ["Thời gian xử lý tại Server (server_processing_ms)", "32 – 45 ms", "< 50 ms", "Rất nhanh trên CPU Intel Core i5 không GPU rời."],
    ["Độ trễ WebSocket trọn vòng (Round-Trip Ping)", "15 – 35 ms", "< 50 ms", "Đường truyền mạng nội bộ phản hồi tức thì."],
    ["Tổng độ trễ từ camera đến giao diện (End-to-End)", "47 – 80 ms", "< 100 ms", "Mắt người hoàn toàn không cảm nhận thấy độ trễ."],
    ["Bộ nhớ RAM tiêu thụ (Backend Server)", "~ 380 MB", "< 1 GB", "Rất nhẹ, vận hành ổn định liên tục nhiều giờ."]
]

TABLE_TASK_ASSIGNMENT = [
    ["Thành viên", "Vai trò đảm nhiệm", "Công việc chính hoàn thành", "Sản phẩm bàn giao cụ thể"],
    ["Dương Ngọc Quang (B24DCKH112)", "Trưởng nhóm / Computer Vision & Machine Learning", "Thu thập dữ liệu thực nghiệm 14 người; thiết kế bộ 12 đặc trưng hình học RAW12; nghiên cứu và huấn luyện 4 mô hình học máy (SVM RBF, RF, XGB, MLP).", "Tập dữ liệu raw, module FeatureExtractor, pipeline huấn luyện, các mô hình học máy đã huấn luyện."],
    ["Hoàng Hữu Mạnh (B24DCKH080)", "Thành viên / Data Processing & Model Evaluation", "Tiền xử lý và làm sạch dữ liệu; xây dựng thuật toán Circular Median; thiết kế giao thức Nested LOPO CV; trực quan hóa ma trận nhầm lẫn và viết tài liệu.", "Dataset CSV đã làm sạch, kết quả đánh giá LOPO, tài liệu kỹ thuật, slide thuyết trình."],
    ["Đặng Xuân Quân (B24DCKH105)", "Thành viên / Application & Backend Integration", "Xây dựng hệ thống Web Dashboard (FastAPI, WebSocket, TailwindCSS); triển khai module TemporalMonitor, Yaw Gating và SessionStatistics; tối ưu độ trễ One-Frame-in-Flight.", "Máy chủ Web thời gian thực, giao diện Dashboard tương tác, chức năng cảnh báo âm thanh/thị giác, bộ Unit Test."]
]

TABLE_AI_APPLICATIONS = [
    ["Giai đoạn phát triển", "Cách thức và Công cụ AI ứng dụng", "Giá trị mang lại cho đề tài", "Quy trình kiểm chứng độc lập của nhóm"],
    ["Nghiên cứu giải pháp", "Tra cứu tài liệu khoa học về Pose Estimation và Ergonomics qua Gemini / ChatGPT.", "Rút ngắn thời gian tổng hợp các phương pháp ước lượng tư thế hiện đại.", "Đối chiếu chéo với các bài báo khoa học gốc trên IEEE và PubMed."],
    ["Thiết kế đặc trưng", "Tham khảo ý tưởng xử lý góc tuần hoàn Circular Median và các đại lượng log-ratio.", "Định hình cấu trúc vector REP13 có khả năng kháng sai lệch vóc dáng.", "Chạy thực nghiệm EDA kiểm chứng độ phân tán chủ thể giảm từ 0.632 xuống 0.418."],
    ["Tối ưu mã nguồn", "Gợi ý tối ưu các phép toán ma trận NumPy và luồng bất đồng bộ FastAPI WebSocket.", "Tăng tốc độ xử lý server từ 65ms xuống dưới 45ms trên CPU.", "Chạy bộ kiểm thử tự động pytest 8 files để đảm bảo không phát sinh lỗi hồi quy."],
    ["Xử lý lỗi hệ thống", "Chẩn đoán nguyên nhân nghẽn hàng đợi WebSocket và gợi ý cơ chế One-Frame-in-Flight.", "Triệt tiêu hiện tượng dồn ứ khung hình, giữ độ trễ luôn ổn định dưới 50ms.", "Thực nghiệm kiểm chứng tải liên tục trong phiên làm việc kéo dài 60 phút."],
    ["Chuẩn hóa tài liệu", "Hỗ trợ định dạng bảng biểu, rà soát văn phong học thuật và cấu trúc báo cáo.", "Báo cáo đạt chuẩn quy cách học thuật của Học viện, trình bày khoa học, chuyên nghiệp.", "Các thành viên trực tiếp rà soát, chỉnh sửa toàn bộ nội dung chuyên môn và số liệu."]
]

print("Loaded all report tables and metadata.")
