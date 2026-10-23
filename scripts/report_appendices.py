"""
Module: report_appendices.py
Dữ liệu và mã nguồn chi tiết cho các Phụ lục A, B, C, D, E.
"""

HYPERPARAMETER_SEARCH_SPACE = [
    ["Thuật toán", "Tên siêu tham số", "Không gian tìm kiếm (Grid Search)", "Ý nghĩa điều chuẩn"],
    ["SVM (Kernel RBF)", "C", "[0.01, 0.1, 1.0, 10.0, 100.0]", "Kiểm soát mức độ phạt các vi phạm phân loại lề."],
    ["SVM (Kernel RBF)", "gamma", "['scale', 'auto', 0.001, 0.01, 0.1, 1.0]", "Xác định bán kính ảnh hưởng của các vector hỗ trợ."],
    ["SVM (Kernel RBF)", "class_weight", "[None, 'balanced']", "Tự động cân bằng trọng số các lớp mất cân bằng."],
    ["Random Forest", "n_estimators", "[100, 200, 400]", "Số lượng cây quyết định trong rừng."],
    ["Random Forest", "max_depth", "[5, 8, 12, None]", "Độ sâu tối đa của mỗi cây nhằm chống overfit."],
    ["Random Forest", "min_samples_split", "[2, 5, 10]", "Số mẫu tối thiểu để tiếp tục phân nhánh node."],
    ["Random Forest", "min_samples_leaf", "[1, 2, 4]", "Số mẫu tối thiểu tại mỗi node lá."],
    ["Random Forest", "max_features", "['sqrt', 'log2']", "Số lượng thuộc tính ngẫu nhiên chọn tại mỗi node."],
    ["Random Forest", "class_weight", "[None, 'balanced']", "Cân bằng trọng số mẫu giữa các lớp."],
    ["XGBoost", "n_estimators", "[100, 150, 250, 400, 600]", "Số vòng lặp boosting tối đa."],
    ["XGBoost", "learning_rate", "[0.02, 0.05, 0.1, 0.2]", "Tốc độ co ngót (shrinkage) của từng cây mới."],
    ["XGBoost", "max_depth", "[3, 5, 7, 9]", "Độ sâu tối đa của các cây boosting."],
    ["XGBoost", "subsample", "[0.7, 0.85, 1.0]", "Tỷ lệ lấy mẫu ngẫu nhiên các dòng dữ liệu."],
    ["XGBoost", "colsample_bytree", "[0.7, 0.85, 1.0]", "Tỷ lệ lấy mẫu ngẫu nhiên các cột đặc trưng."],
    ["XGBoost", "reg_alpha (L1)", "[0, 0.01, 0.1, 1.0]", "Hệ số điều chuẩn L1 tạo độ thưa (sparsity)."],
    ["XGBoost", "reg_lambda (L2)", "[0.5, 1.0, 2.0, 5.0]", "Hệ số điều chuẩn L2 kiểm soát trọng số lá cây."],
    ["Đa tầng nơ-ron (MLP)", "hidden_layer_sizes", "[(64, 32), (128, 64), (128, 64, 32)]", "Kiến trúc các tầng ẩn và số lượng nơ-ron."],
    ["Đa tầng nơ-ron (MLP)", "activation", "['relu', 'tanh']", "Hàm kích hoạt phi tuyến giữa các tầng."],
    ["Đa tầng nơ-ron (MLP)", "alpha (L2 penalty)", "[0.0001, 0.001, 0.01]", "Hệ số suy giảm trọng số (weight decay)."],
    ["Đa tầng nơ-ron (MLP)", "learning_rate_init", "[0.001, 0.01]", "Tốc độ học ban đầu của thuật toán Adam."],
    ["Đa tầng nơ-ron (MLP)", "max_iter", "[300, 500]", "Số chu kỳ lan truyền xuôi/ngược tối đa."]
]

OPTIMAL_PARAMS = [
    ["Mô hình", "Bộ siêu tham số tối ưu chốt cho Production", "LOPO Macro F1", "OOF Accuracy"],
    ["SVM (Kernel RBF)", "C = 1.0, gamma = 0.01, class_weight = 'balanced'", "0.9199", "0.9369"],
    ["Random Forest", "n_estimators = 400, max_depth = 8, min_samples_split = 10, min_samples_leaf = 2, max_features = 'log2', class_weight = 'balanced'", "0.8993", "0.9159"],
    ["MLP Classifier", "hidden_layer_sizes = (128, 64), activation = 'relu', alpha = 0.001, learning_rate_init = 0.001, max_iter = 300", "0.8991", "0.9171"],
    ["XGBoost", "n_estimators = 250, learning_rate = 0.05, max_depth = 5, subsample = 0.85, colsample_bytree = 0.7, reg_alpha = 0.1, reg_lambda = 2.0", "0.8736", "0.8947"]
]

HARDWARE_CONFIG = [
    ["Hạng mục phần cứng / phần mềm", "Thông số cấu hình môi trường thực nghiệm"],
    ["Vi xử lý (CPU)", "Intel® Core™ i5-1135G7 @ 2.40GHz (4 nhân, 8 luồng, Turbo Boost 4.20GHz)"],
    ["Bộ nhớ RAM", "16 GB DDR4 Bus 3200 MHz (Bộ nhớ tiêu thụ thực tế của hệ thống: ~380 MB)"],
    ["Bộ xử lý đồ họa (GPU)", "Intel® Iris® Xe Graphics tích hợp (Hệ thống chạy 100% trên CPU, không đòi hỏi GPU rời)"],
    ["Ổ cứng lưu trữ", "512 GB SSD NVMe M.2 PCIe Gen 3x4"],
    ["Hệ điều hành", "Microsoft Windows 10 / 11 Pro 64-bit"],
    ["Môi trường thực thi Python", "Python 3.10 / 3.13 64-bit"],
    ["Camera thu nhận hình ảnh", "Webcam tích hợp tiêu chuẩn laptop HD 720p (30 FPS, góc đặt 45° chếch bên trái)"]
]

LOPO_FOLDS_SVM_RBF = [
    ["Fold", "Đối tượng Test", "N_train", "N_test", "Siêu tham số tối ưu (Inner Fold)", "Accuracy", "Precision", "Recall", "Macro F1", "Correct F1"],
    ["Fold 1", "person01", "3,838", "138", "C=0.1, gamma='scale', balanced", "1.0000", "1.0000", "1.0000", "1.0000", "1.0000"],
    ["Fold 2", "person02", "3,705", "271", "C=0.1, gamma='scale', balanced", "0.7048", "0.7667", "0.6767", "0.6719", "0.6667"],
    ["Fold 3", "person03", "3,776", "200", "C=1.0, gamma=0.01, balanced", "0.9550", "0.9528", "0.9415", "0.9434", "0.9910"],
    ["Fold 4", "person04", "3,702", "274", "C=0.1, gamma=0.1, balanced", "0.8759", "0.9115", "0.8813", "0.8787", "0.7848"],
    ["Fold 5", "person05", "3,717", "259", "C=0.1, gamma=0.1, balanced", "0.9923", "0.9932", "0.9921", "0.9925", "0.9863"],
    ["Fold 6", "person06", "3,737", "239", "C=1.0, gamma=0.01, balanced", "0.9163", "0.9379", "0.8605", "0.8719", "0.9420"],
    ["Fold 7", "person07", "3,182", "794", "C=1.0, gamma=0.01, None", "0.9899", "0.9903", "0.9897", "0.9900", "0.9881"],
    ["Fold 8", "person08", "3,743", "233", "C=0.1, gamma=0.1, None", "1.0000", "1.0000", "1.0000", "1.0000", "1.0000"],
    ["Fold 9", "person09", "3,703", "273", "C=0.1, gamma='scale', balanced", "0.9780", "0.9811", "0.9787", "0.9796", "0.9647"],
    ["Fold 10", "person10", "3,666", "310", "C=0.1, gamma='scale', balanced", "0.9452", "0.9401", "0.9574", "0.9436", "1.0000"],
    ["Fold 11", "person11", "3,751", "225", "C=0.1, gamma='scale', balanced", "0.9556", "0.9473", "0.9163", "0.9297", "0.8333"],
    ["Fold 12", "person12", "3,722", "254", "C=0.1, gamma='scale', None", "0.9882", "0.9893", "0.9879", "0.9884", "0.9839"],
    ["Fold 13", "person13", "3,719", "257", "C=0.1, gamma=0.1, None", "0.7588", "0.8760", "0.7615", "0.6896", "1.0000"],
    ["Fold 14", "person14", "3,727", "249", "C=0.1, gamma='scale', balanced", "1.0000", "1.0000", "1.0000", "1.0000", "1.0000"],
    ["Trung bình (Mean)", "14 Folds", "3,684", "284", "C=1.0, gamma=0.01, balanced", "0.9329", "0.9493", "0.9248", "0.9199", "0.9381"]
]

PER_PERSON_COMPARISON = [
    ["Mã cá nhân (Person ID)", "Số mẫu đánh giá", "SVM (Kernel RBF)", "Random Forest", "Đa tầng nơ-ron (MLP)", "XGBoost", "Nhận xét đặc thù dáng ngồi"],
    ["person01", "138", "1.0000", "1.0000", "1.0000", "1.0000", "Dáng chuẩn rõ nét, biên độ các tư thế phân tách rạch ròi."],
    ["person02", "271", "0.6719", "0.6444", "0.6187", "0.6498", "Worst-case: Dáng gù tự nhiên có biên độ dịch chuyển nhỏ hơn mức trung bình."],
    ["person03", "200", "0.9434", "0.9240", "0.9227", "0.9013", "Tư thế ngồi thẳng lưng và nghiêng rõ rệt."],
    ["person04", "274", "0.8787", "0.6620", "0.8972", "0.6315", "SVM và MLP vượt trội hoàn toàn so với các mô hình cây (RF, XGB)."],
    ["person05", "259", "0.9925", "0.9841", "0.8069", "0.6921", "SVM đạt độ chính xác gần như tuyệt đối."],
    ["person06", "239", "0.8719", "0.8396", "0.9374", "0.8610", "MLP và SVM phân loại rất tốt các góc nghiêng đầu."],
    ["person07", "794", "0.9899", "0.9899", "0.9900", "0.9846", "Tập dữ liệu lớn nhất (3 sessions) chứng minh tính bền vững của Baseline."],
    ["person08", "233", "1.0000", "0.9916", "0.9876", "0.9620", "Dữ liệu thu mới đạt điểm tuyệt đối trên SVM."],
    ["person09", "273", "0.9796", "0.9734", "0.9706", "0.9510", "Các tư thế phân tách rất đẹp trên không gian REP13."],
    ["person10", "310", "0.9436", "0.9813", "0.9405", "0.9813", "Mô hình cây và SVM đều đạt hiệu năng xuất sắc."],
    ["person11", "225", "0.9297", "0.9699", "0.8508", "0.9816", "Dữ liệu thu lại đạt độ chính xác cao trên mọi mô hình."],
    ["person12", "254", "0.9884", "0.9687", "1.0000", "0.9727", "MLP và SVM đạt độ chính xác xấp xỉ 100%."],
    ["person13", "257", "0.6896", "0.6649", "0.6649", "0.6612", "Đối tượng có chiều cao lớn, khoảng cách camera cần điều chỉnh."],
    ["person14", "249", "1.0000", "0.9957", "1.0000", "1.0000", "Đạt điểm tuyệt đối 1.0000 trên SVM, MLP và XGBoost."],
    ["Trung bình (Macro Mean)", "3,976", "0.9199", "0.8993", "0.8991", "0.8736", "SVM RBF là mô hình chiến thắng toàn diện."]
]

CODE_SNIPPETS = {
    "feature_extractor": '''# src/feature_extractor.py (Trích xuất 12 đặc trưng hình học thô RAW12)
import numpy as np

class FeatureExtractor:
    FEATURE_NAMES = [
        "shoulder_roll_deg", "eye_roll_deg", "head_shoulder_roll_diff_deg",
        "neck_pitch_deg", "eye_center_x_px", "eye_center_y_px",
        "shoulder_center_x_px", "eye_shoulder_vertical_gap_px",
        "eye_shoulder_horizontal_offset_px", "inter_eye_distance_px",
        "ear_nose_horizontal_span_px", "shoulder_width_px"
    ]

    def extract_raw_features(self, keypoints: np.ndarray) -> np.ndarray:
        """Trích xuất vector 12 đặc trưng hình học từ 6 điểm keypoints."""
        # 0: Nose, 1: Left Eye, 2: Right Eye, 3: Left Ear, 5: Left Shoulder, 6: Right Shoulder
        nose, le, re, lear, ls, rs = keypoints[0], keypoints[1], keypoints[2], keypoints[3], keypoints[5], keypoints[6]

        # 1. Nhóm hướng (Orientation)
        shoulder_roll = np.arctan2(rs[1] - ls[1], rs[0] - ls[0]) * 180.0 / np.pi
        eye_roll = np.arctan2(re[1] - le[1], re[0] - le[0]) * 180.0 / np.pi
        diff_roll = (eye_roll - shoulder_roll + 180.0) % 360.0 - 180.0

        # 2. Nhóm mặt đứng dọc (Sagittal proxy)
        neck_pitch = np.arctan2(nose[1] - lear[1], nose[0] - lear[0]) * 180.0 / np.pi

        # 3. Nhóm không gian (Spatial)
        eye_center = (le[:2] + re[:2]) / 2.0
        shoulder_center = (ls[:2] + rs[:2]) / 2.0
        vert_gap = shoulder_center[1] - eye_center[1]
        horiz_offset = eye_center[0] - shoulder_center[0]

        # 4. Nhóm tỷ lệ & phối cảnh (Perspective proxy)
        eye_dist = np.linalg.norm(re[:2] - le[:2])
        ear_nose_span = np.abs(nose[0] - lear[0])
        shoulder_width = np.linalg.norm(rs[:2] - ls[:2])

        return np.array([
            shoulder_roll, eye_roll, diff_roll, neck_pitch,
            eye_center[0], eye_center[1], shoulder_center[0],
            vert_gap, horiz_offset, eye_dist, ear_nose_span, shoulder_width
        ], dtype=np.float32)
''',

    "personal_calibration": '''# src/personal_calibration.py (Cơ chế Circular Median và Baseline cá nhân)
import numpy as np

class PersonalCalibration:
    ANGLE_INDICES = [0, 1, 2, 3]

    def _circular_median(self, angles_deg: np.ndarray) -> float:
        """Tính trung vị góc tuần hoàn trên đường tròn [-180, 180)."""
        angles_rad = np.deg2rad(angles_deg)
        # Tìm góc tham chiếu có tổng khoảng cách góc tới các mẫu khác là nhỏ nhất
        diffs = np.abs((angles_rad[:, None] - angles_rad[None, :] + np.pi) % (2 * np.pi) - np.pi)
        med_idx = np.argmin(np.sum(diffs, axis=1))
        ref_angle = angles_rad[med_idx]
        
        # Mở rộng các góc quanh mốc tham chiếu và tính trung vị tuyến tính
        unwrapped = (angles_rad - ref_angle + np.pi) % (2 * np.pi) - np.pi + ref_angle
        med_rad = np.median(unwrapped)
        return float(np.rad2deg((med_rad + np.pi) % (2 * np.pi) - np.pi))

    def compute_baseline(self, samples_30x12: np.ndarray) -> np.ndarray:
        """Tính vector 12 đặc trưng Baseline từ 30 mẫu correct hợp lệ."""
        baseline = np.zeros(12, dtype=np.float32)
        for j in range(12):
            if j in self.ANGLE_INDICES:
                baseline[j] = self._circular_median(samples_30x12[:, j])
            else:
                baseline[j] = float(np.median(samples_30x12[:, j]))
        return baseline
''',

    "representation_builder": '''# src/representation_builder.py (Biến đổi RAW12 + Baseline thành REP13)
import numpy as np

class RepresentationBuilder:
    def transform(self, raw12: np.ndarray, baseline: np.ndarray) -> np.ndarray:
        """Biến đổi RAW12 hiện tại so với baseline cá nhân thành vector REP13."""
        rep = np.zeros(13, dtype=np.float32)
        w0 = max(float(baseline[11]), 1e-4) # Chiều rộng vai tham chiếu (W_0)

        # 1. 4 đặc trưng hiệu số góc có xử lý tuần hoàn [-180, 180)
        for i in range(4):
            rep[i] = (raw12[i] - baseline[i] + 180.0) % 360.0 - 180.0

        # 2. 5 đặc trưng không gian chuẩn hóa theo độ rộng vai tham chiếu W_0
        for i in range(4, 9):
            rep[i] = (raw12[i] - baseline[i]) / w0

        # 3. 3 đặc trưng log-ratio khoảng cách biểu kiến
        rep[9] = np.log(max(raw12[9], 1e-4) / max(baseline[9], 1e-4))
        rep[10] = np.log(max(raw12[10], 1e-4) / max(baseline[10], 1e-4))
        rep[11] = np.log(max(raw12[11], 1e-4) / max(baseline[11], 1e-4))

        # 4. Đặc trưng tổng hợp độ lớn dịch chuyển đầu
        rep[12] = np.sqrt(rep[4]**2 + rep[5]**2)

        return rep
''',

    "temporal_monitor": '''# src/temporal_monitor.py (Làm mượt thời gian, Hysteresis và Yaw Gating)
from collections import deque, Counter

class TemporalMonitor:
    def __init__(self, window_size=7, hysteresis_frames=2, min_samples=3):
        self.window = deque(maxlen=window_size)
        self.hysteresis_frames = hysteresis_frames
        self.min_samples = min_samples
        self.stable_posture = "evaluating"
        self.candidate_posture = None
        self.candidate_count = 0

    def process(self, raw_label: str, eye_nose_ratio: float = None) -> str:
        # Cơ chế Yaw Gating: Khử nhiễu khi người dùng quay mặt
        if eye_nose_ratio is not None and (eye_nose_ratio < 0.45 or eye_nose_ratio > 1.80):
            return self.stable_posture # Khóa trạng thái thân cũ, không nhận cảnh báo giả

        if raw_label not in ["correct", "forward_slouch", "lean_left", "lean_right"]:
            return self.stable_posture

        self.window.append(raw_label)
        if len(self.window) < self.min_samples:
            return "evaluating"

        # Majority Vote (Bầu chọn số đông trong cửa sổ trượt)
        majority_winner = Counter(self.window).most_common(1)[0][0]

        # Khởi tạo trạng thái đầu tiên
        if self.stable_posture == "evaluating":
            self.stable_posture = majority_winner
            return self.stable_posture

        # Hysteresis (Độ trễ chuyển đổi trạng thái)
        if majority_winner != self.stable_posture:
            if majority_winner == self.candidate_posture:
                self.candidate_count += 1
                if self.candidate_count >= self.hysteresis_frames:
                    self.stable_posture = majority_winner
                    self.candidate_posture = None
                    self.candidate_count = 0
            else:
                self.candidate_posture = majority_winner
                self.candidate_count = 1
        else:
            self.candidate_posture = None
            self.candidate_count = 0

        return self.stable_posture
''',

    "session_statistics": '''# src/session_statistics.py (Tính Điểm Công thái học và Đợt vi phạm)
import time

class SessionStatistics:
    def __init__(self, alert_threshold_sec=2.0):
        self.alert_threshold = alert_threshold_sec
        self.t_correct = 0.0
        self.t_bad = 0.0
        self.violation_episodes = 0
        self.in_violation = False
        self.bad_posture_start = None

    def update(self, current_posture: str, dt: float) -> bool:
        """Cập nhật trạng thái và trả về True nếu kích hoạt chuông cảnh báo."""
        trigger_alert = False
        if current_posture == "correct":
            self.t_correct += dt
            self.in_violation = False
            self.bad_posture_start = None
        elif current_posture in ["forward_slouch", "lean_left", "lean_right"]:
            self.t_bad += dt
            if self.bad_posture_start is None:
                self.bad_posture_start = time.monotonic()
            
            # Kiểm tra vượt ngưỡng vi phạm liên tục (Violation Episode)
            elapsed = time.monotonic() - self.bad_posture_start
            if elapsed >= self.alert_threshold and not self.in_violation:
                self.in_violation = True
                self.violation_episodes += 1
                trigger_alert = True
        return trigger_alert

    def compute_ergonomics_score(self) -> float:
        """Tính điểm sức khỏe phiên ngồi từ 0 đến 100 điểm."""
        total_time = self.t_correct + self.t_bad
        if total_time <= 0.0:
            return 100.0
        ratio = (self.t_correct / total_time) * 100.0
        penalty = self.violation_episodes * 2.0
        return max(0.0, min(100.0, ratio - penalty))
'''
}

print("Loaded all report appendices data.")
