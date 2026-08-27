# ⚡ Smart Roommate Expense & Utility Splitter

A production-ready, mobile-responsive web application that simplifies shared household budgeting and features a dynamic, multi-tiered electricity tariff matrix.

🔗 **[Click Here to Run My App Live!](https://roommate-expense-splitter-yh5udehmqcxc9gyf47jw99.streamlit.app/)**

---

## 🧬 My Journey: Biology to ECE
As a first-year Electronics and Communication Engineering (ECE) student transitioning from a biological sciences background, this project highlights my rapid adaptation to programming logic. To challenge myself further, I built, tested, and successfully deployed this entire application using only my **smartphone**.

## 🚀 Advanced UI/UX & Engineering Features
Unlike standard calculators, this project implements a custom **Conditional Rendering Interface**:
- **Dynamic Input Fields:** The app actively reads the total electricity units entered. If you enter `150 units`, it clean-renders *only* the input for Bracket A. The fields for Brackets B through E stay completely hidden until your consumption scales past those thresholds.
- **Null Safety Verification:** Built logic gates to ensure that empty state parameters (`None` type values) do not trigger runtime calculation errors or software crashes.
- **Mathematical Multi-Tier Logic:** Seamlessly handles non-linear conditional branching math to calculate electricity slabs accurately.

## 🛠️ Built With
- **Language:** Python 3
- **Framework:** Streamlit (Web Architecture Engine)
- **Deployment Platform:** Streamlit Community Cloud

## 📂 Repository Layout
- `app.py` - The core application file featuring dynamic UI logic and calculation matrices.
- `requirements.txt` - Configuration manifest directing the server to install necessary dependencies.
- `README.md` - Technical project documentation.
