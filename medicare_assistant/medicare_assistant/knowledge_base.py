from dotenv import load_dotenv
import os

load_dotenv()

DOCUMENTS = [
    {
        "id": "doc_001",
        "topic": "OPD Timings",
        "text": (
            "MediCare General Hospital OPD Timings\n\n"
            "MediCare General Hospital operates Outpatient Department (OPD) services six days a week with "
            "comprehensive coverage across all specialty departments.\n\n"
            "Regular OPD Hours (Monday to Saturday): 8:00 AM to 8:00 PM\n"
            "Sunday OPD Hours: 9:00 AM to 1:00 PM (Emergency consultations only)\n\n"
            "Department-wise OPD Schedule:\n"
            "- Cardiology: Monday to Saturday, 8:00 AM to 8:00 PM (individual doctor timings may vary)\n"
            "- Orthopedics: Monday to Saturday, 8:00 AM to 8:00 PM\n"
            "- Neurology: Monday to Saturday, 8:00 AM to 8:00 PM\n"
            "- Pediatrics: Daily (including Sunday), 9:00 AM to 12:00 PM\n"
            "- General Medicine: Monday to Saturday, 8:00 AM to 8:00 PM\n"
            "- Gynecology and Obstetrics: Monday to Saturday, 8:00 AM to 8:00 PM\n"
            "- Dermatology: Monday to Saturday, 8:00 AM to 6:00 PM\n"
            "- ENT (Ear, Nose and Throat): Monday to Saturday, 8:00 AM to 6:00 PM\n"
            "- Ophthalmology: Monday to Saturday, 8:00 AM to 6:00 PM\n"
            "- Psychiatry: Monday to Friday, 9:00 AM to 5:00 PM\n"
            "- Urology: Monday to Saturday, 8:00 AM to 6:00 PM\n"
            "- Gastroenterology: Monday to Saturday, 9:00 AM to 5:00 PM\n\n"
            "On Sundays, only emergency OPD and Pediatrics OPD are available from 9:00 AM to 1:00 PM. "
            "All other specialty OPDs are closed on Sundays.\n\n"
            "Patients are advised to arrive at least 15 minutes before their scheduled appointment. "
            "Token numbers are issued at the OPD registration counter from 7:45 AM on weekdays.\n\n"
            "For the latest schedule or special holiday timings, please call the hospital helpline at 040-99887766."
        ),
    },
    {
        "id": "doc_002",
        "topic": "Emergency Services",
        "text": (
            "MediCare General Hospital Emergency Services\n\n"
            "MediCare General Hospital provides round-the-clock emergency medical care, 24 hours a day, "
            "7 days a week, 365 days a year.\n\n"
            "Emergency Contact Number: 040-12345678 (available 24/7)\n"
            "Main Helpline: 040-99887766\n\n"
            "Emergency Department Features:\n"
            "- Fully staffed 24/7 Emergency Department with senior residents and consultants on call\n"
            "- Dedicated Trauma Care Unit for accident victims and multi-trauma patients\n"
            "- 24-bed Intensive Care Unit (ICU) with advanced life support systems\n"
            "- Cardiac Intensive Care Unit (CICU) for cardiac emergencies\n"
            "- Pediatric Emergency services available round the clock\n"
            "- Neonatal Intensive Care Unit (NICU) for critical newborns\n"
            "- Stroke management protocol with CT scan and MRI available 24/7\n\n"
            "Ambulance Services:\n"
            "- Advanced Life Support (ALS) ambulances available 24/7\n"
            "- Basic Life Support (BLS) ambulances for patient transfers\n"
            "- Ambulance booking: Call 040-12345678\n"
            "- GPS-tracked fleet for faster response\n\n"
            "Emergency Conditions Handled:\n"
            "- Heart attacks and cardiac emergencies\n"
            "- Stroke and neurological emergencies\n"
            "- Road traffic accidents and trauma\n"
            "- Severe breathing difficulties and respiratory emergencies\n"
            "- Poisoning and drug overdose cases\n"
            "- Obstetric emergencies and complicated deliveries\n"
            "- Pediatric emergencies including high fever and seizures\n\n"
            "Triage System: Patients are assessed using a color-coded triage system (Red/Orange/Yellow/Green) "
            "to prioritize care based on severity.\n\n"
            "If you or someone near you is experiencing a medical emergency, call 040-12345678 immediately. "
            "Do not wait — every second counts in a medical emergency."
        ),
    },
    {
        "id": "doc_003",
        "topic": "Doctor Directory - Cardiology",
        "text": (
            "MediCare General Hospital — Cardiology Department\n\n"
            "The Cardiology Department at MediCare General Hospital offers comprehensive cardiac care "
            "with a team of highly qualified cardiologists.\n\n"
            "Dr. Suresh Reddy\n"
            "- Qualifications: MBBS, MD (Internal Medicine), DM (Cardiology)\n"
            "- Specialization: Interventional Cardiology, Coronary Angioplasty, Pacemaker Implantation\n"
            "- OPD Schedule: Monday, Wednesday, and Friday — 10:00 AM to 2:00 PM\n"
            "- Experience: 18 years in interventional cardiology\n"
            "- Languages: Telugu, Hindi, English\n\n"
            "Dr. Anitha Rao\n"
            "- Qualifications: MBBS, MD (Cardiology)\n"
            "- Specialization: Non-invasive Cardiology, Echocardiography, Heart Failure Management\n"
            "- OPD Schedule: Tuesday and Thursday — 9:00 AM to 1:00 PM\n"
            "- Experience: 12 years in clinical cardiology\n"
            "- Languages: Telugu, English\n\n"
            "Dr. Prakash Kumar\n"
            "- Qualifications: MBBS, DM (Cardiology)\n"
            "- Specialization: Electrophysiology, Cardiac Arrhythmias, Ablation Procedures\n"
            "- OPD Schedule: Saturday — 10:00 AM to 12:00 PM\n"
            "- Experience: 10 years in cardiac electrophysiology\n"
            "- Languages: Hindi, English, Tamil\n\n"
            "Services offered by the Cardiology Department:\n"
            "- ECG (Electrocardiogram)\n"
            "- Echocardiography (2D Echo)\n"
            "- Stress Test (TMT)\n"
            "- Holter Monitoring\n"
            "- Coronary Angiography\n"
            "- Angioplasty and Stenting\n"
            "- Pacemaker and ICD Implantation\n\n"
            "For appointments, call: 040-99887766 or book online at the hospital website."
        ),
    },
    {
        "id": "doc_004",
        "topic": "Doctor Directory - Orthopedics",
        "text": (
            "MediCare General Hospital — Orthopedics Department\n\n"
            "The Orthopedics Department at MediCare General Hospital specializes in bone, joint, spine, "
            "and sports injury treatment.\n\n"
            "Dr. Ramesh Naidu\n"
            "- Qualifications: MBBS, MS (Orthopedics)\n"
            "- Specialization: Joint Replacement Surgery (Hip, Knee), Spine Surgery, Sports Injuries\n"
            "- OPD Schedule: Monday to Friday — 9:00 AM to 1:00 PM\n"
            "- Experience: 20 years in orthopedic surgery\n"
            "- Notable: Performed 1000+ knee replacement surgeries\n"
            "- Languages: Telugu, Hindi, English\n\n"
            "Dr. Shalini Verma\n"
            "- Qualifications: MBBS, MS (Orthopedics)\n"
            "- Specialization: Pediatric Orthopedics, Fracture Management, Arthroscopy\n"
            "- OPD Schedule: Tuesday, Thursday, and Saturday — 2:00 PM to 6:00 PM\n"
            "- Experience: 14 years in orthopedic surgery with focus on pediatric cases\n"
            "- Languages: Hindi, English, Telugu\n\n"
            "Services offered by the Orthopedics Department:\n"
            "- Fracture treatment and casting\n"
            "- Joint replacement surgery (hip, knee, shoulder)\n"
            "- Arthroscopic surgery for knee and shoulder\n"
            "- Spine surgery for disc herniation and deformities\n"
            "- Sports injury rehabilitation\n"
            "- Pediatric orthopedic care\n"
            "- Bone density testing\n"
            "- Physiotherapy and rehabilitation services\n\n"
            "The department is equipped with a state-of-the-art operation theater, digital X-ray, MRI, "
            "and CT scan facilities.\n\n"
            "For appointments with Dr. Ramesh Naidu or Dr. Shalini Verma, call: 040-99887766."
        ),
    },
    {
        "id": "doc_005",
        "topic": "Doctor Directory - Neurology and Pediatrics",
        "text": (
            "MediCare General Hospital — Neurology and Pediatrics Departments\n\n"
            "NEUROLOGY DEPARTMENT\n\n"
            "Dr. Arun Sharma\n"
            "- Qualifications: MBBS, DM (Neurology)\n"
            "- Specialization: Epilepsy, Stroke Management, Headache Disorders, Movement Disorders (Parkinson's Disease)\n"
            "- OPD Schedule: Monday, Wednesday, and Friday — 11:00 AM to 3:00 PM\n"
            "- Experience: 15 years in clinical neurology\n"
            "- Languages: Hindi, English, Telugu\n\n"
            "Neurology Services:\n"
            "- EEG (Electroencephalogram)\n"
            "- EMG/NCS (Nerve Conduction Studies)\n"
            "- Brain MRI and CT Scan\n"
            "- Stroke thrombolysis and intervention\n"
            "- Epilepsy monitoring unit\n"
            "- Botox therapy for migraine and movement disorders\n"
            "- Memory clinic for dementia assessment\n\n"
            "PEDIATRICS DEPARTMENT\n\n"
            "Dr. Kavitha Iyer\n"
            "- Qualifications: MBBS, MD (Pediatrics)\n"
            "- Specialization: General Pediatrics, Neonatology, Developmental Pediatrics, Childhood Infections\n"
            "- OPD Schedule: Daily (Monday to Sunday) — 9:00 AM to 12:00 PM\n"
            "- Experience: 16 years in pediatrics and neonatology\n"
            "- Languages: Tamil, Telugu, English, Hindi\n\n"
            "Pediatrics Services:\n"
            "- Well-baby checkups and vaccination\n"
            "- Growth and development monitoring\n"
            "- Neonatal care (NICU)\n"
            "- Management of childhood illnesses (fever, respiratory infections, diarrhea)\n"
            "- Asthma and allergy management in children\n"
            "- Nutritional counseling\n"
            "- School health screening\n\n"
            "Both departments are available for emergency consultations 24/7. "
            "For appointments, call: 040-99887766."
        ),
    },
    {
        "id": "doc_006",
        "topic": "Appointment Booking",
        "text": (
            "MediCare General Hospital — Appointment Booking Process\n\n"
            "MediCare General Hospital offers multiple convenient ways to book appointments "
            "with our specialist doctors.\n\n"
            "Appointment Booking Methods:\n\n"
            "1. Walk-in: Patients can directly visit the OPD registration counter at the hospital. "
            "Tokens are issued on a first-come, first-served basis. Registration counter opens at "
            "7:45 AM on weekdays and 8:00 AM on Saturdays.\n\n"
            "2. Phone Booking: Call our central appointment number 040-99887766. Our team is available "
            "Monday to Saturday, 8:00 AM to 8:00 PM. For Sunday emergencies, call 040-12345678.\n\n"
            "3. Online Booking: Visit the hospital's official website to book appointments online. "
            "You can select your preferred doctor, date, and time slot. "
            "Confirmation is sent via SMS and email.\n\n"
            "4. Token System: All OPD appointments use a token-based queuing system. "
            "Each token represents a 15-minute consultation slot. "
            "Patients with prior appointments are given priority over walk-in tokens.\n\n"
            "Appointment Slot Details:\n"
            "- Each consultation slot is 15 minutes\n"
            "- For new patients: Please arrive 20 minutes before your token time\n"
            "- For follow-up patients: Carry previous prescriptions and reports\n"
            "- Token cancellation: Please cancel at least 2 hours in advance\n\n"
            "Appointment Reminders:\n"
            "- Automated SMS reminders are sent 24 hours before the appointment\n"
            "- WhatsApp reminders are available for registered patients\n\n"
            "Special Assistance:\n"
            "- Differently-abled patients and senior citizens (above 70 years) receive priority token allocation\n"
            "- For patients requiring interpreter services, inform the registration desk in advance\n\n"
            "For any appointment-related queries, call: 040-99887766."
        ),
    },
    {
        "id": "doc_007",
        "topic": "Consultation Fees",
        "text": (
            "MediCare General Hospital — Consultation Fees and Charges\n\n"
            "MediCare General Hospital maintains transparent and standardized fee structures "
            "for all outpatient consultations.\n\n"
            "OPD Consultation Fees:\n"
            "- General OPD (General Medicine, Family Physician): Rs.300 per consultation\n"
            "- Specialist Consultation (Orthopedics, Dermatology, ENT, Ophthalmology, Gynecology, "
            "Psychiatry, Urology, Gastroenterology): Rs.500 per consultation\n"
            "- Super-specialist Consultation (Cardiology, Neurology, Cardiothoracic Surgery, "
            "Neurosurgery): Rs.800 per consultation\n"
            "- Emergency OPD Consultation: Rs.500\n"
            "- Pediatrics OPD: Rs.400 per consultation\n\n"
            "Follow-up Charges:\n"
            "- Follow-up consultation within 7 days of first visit: Rs.150 (with the same doctor)\n"
            "- Follow-up after 7 days: Regular consultation fee applies\n\n"
            "Additional Charges:\n"
            "- Procedure charges are separate from consultation fees\n"
            "- Diagnostic tests (blood tests, X-ray, ECG, etc.) are charged additionally\n"
            "- Report review consultation (without full examination): Rs.200\n\n"
            "Payment Methods Accepted:\n"
            "- Cash\n"
            "- Credit and Debit Cards (Visa, Mastercard, RuPay)\n"
            "- UPI payments (Google Pay, PhonePe, Paytm, BHIM)\n"
            "- Net Banking\n"
            "- Insurance cashless (for empanelled insurers)\n\n"
            "Receipts are provided for all payments. For insurance patients, a pre-authorization "
            "letter is required before the consultation.\n\n"
            "For fee-related queries, contact the billing counter or call: 040-99887766."
        ),
    },
    {
        "id": "doc_008",
        "topic": "Insurance and Cashless Services",
        "text": (
            "MediCare General Hospital — Insurance and Cashless Services\n\n"
            "MediCare General Hospital is empanelled with major health insurance companies "
            "to provide cashless treatment to insured patients.\n\n"
            "Empanelled Insurance Companies:\n"
            "1. Star Health and Allied Insurance\n"
            "2. HDFC Ergo Health Insurance\n"
            "3. United India Insurance Company\n"
            "4. New India Assurance Company\n"
            "5. Medi Assist (TPA — Third Party Administrator)\n\n"
            "Additional empanelled networks: ICICI Lombard (select plans), Bajaj Allianz (select plans), "
            "and government health schemes including CGHS, ECHS, and Ayushman Bharat (PMJAY).\n\n"
            "Cashless Admission Process:\n"
            "1. Inform the TPA desk at the time of registration\n"
            "2. Submit your health insurance card and photo ID\n"
            "3. Hospital will initiate pre-authorization with your insurer\n"
            "4. Pre-authorization is required before planned procedures and hospitalizations\n"
            "5. Emergency cashless admissions are processed within 2 hours\n\n"
            "TPA Desk Information:\n"
            "- Location: Ground Floor, near the main registration counter\n"
            "- Timings: Monday to Saturday, 8:00 AM to 8:00 PM\n"
            "- Contact: 040-99887766 (Extension 105)\n"
            "- For after-hours emergency cashless: Duty Manager on call\n\n"
            "Documents Required for Cashless:\n"
            "- Original health insurance card or e-card\n"
            "- Government-issued photo ID (Aadhaar, Passport, Voter ID)\n"
            "- Doctor's referral letter (for planned hospitalization)\n"
            "- Previous discharge summary (if applicable)\n\n"
            "Reimbursement Claims:\n"
            "For non-empanelled insurers, patients pay upfront and get reimbursement from their insurer. "
            "The hospital provides all necessary documents including bills, discharge summary, "
            "and investigation reports.\n\n"
            "For insurance queries, contact: 040-99887766 (Ext. 105)."
        ),
    },
    {
        "id": "doc_009",
        "topic": "Pharmacy Services",
        "text": (
            "MediCare General Hospital — In-House Pharmacy\n\n"
            "MediCare General Hospital's in-house pharmacy provides round-the-clock pharmaceutical "
            "services to patients and their attendants.\n\n"
            "Pharmacy Timings:\n"
            "- Open 24 hours, 7 days a week (including holidays)\n"
            "- No closure on Sundays or public holidays\n\n"
            "Pharmacy Services:\n\n"
            "1. Prescription Medicines:\n"
            "   - A valid prescription from a registered medical practitioner is mandatory for prescription drugs\n"
            "   - Prescriptions from MediCare doctors are processed on priority\n"
            "   - Prescriptions from outside hospitals are also accepted (with original prescription)\n\n"
            "2. Generic Medicine Alternatives:\n"
            "   - Pharmacists provide generic alternatives for branded medicines upon request\n"
            "   - Generic medicines are typically 40-80% cheaper than branded equivalents\n"
            "   - Quality is equivalent as all generics stocked are Jan Aushadhi or WHO-GMP certified\n\n"
            "3. Home Delivery:\n"
            "   - Available for patients on long-term or chronic medications\n"
            "   - Monthly medicine packages can be prepared and home-delivered\n"
            "   - Delivery available within Hyderabad limits (GHMC area)\n"
            "   - Delivery charges: Rs.50 per order (free for orders above Rs.500)\n"
            "   - Call to arrange: 040-99887755\n\n"
            "4. Stocked Items:\n"
            "   - Prescription and OTC medicines\n"
            "   - Surgical supplies and dressings\n"
            "   - Medical devices (BP monitors, glucometers, thermometers)\n"
            "   - Nutritional supplements and infant formula\n"
            "   - Orthopaedic supports and braces\n\n"
            "Pharmacy Contact: 040-99887755\n\n"
            "Location: Ground Floor, adjacent to the main OPD registration area."
        ),
    },
    {
        "id": "doc_010",
        "topic": "Diagnostic Lab Services",
        "text": (
            "MediCare General Hospital — Diagnostic Laboratory Services\n\n"
            "MediCare General Hospital's NABL-accredited diagnostic laboratory offers comprehensive "
            "pathology, radiology, and clinical laboratory testing services.\n\n"
            "Lab Timings:\n"
            "- Monday to Saturday: 6:00 AM to 8:00 PM\n"
            "- Sunday: 7:00 AM to 12:00 PM (noon)\n"
            "- Emergency tests are processed 24/7\n\n"
            "Lab Services Available:\n\n"
            "Blood Tests:\n"
            "- Complete Blood Count (CBC), Blood Sugar, Lipid Profile\n"
            "- Liver Function Tests (LFT), Kidney Function Tests (KFT)\n"
            "- Thyroid Function Tests, Hormone panels\n"
            "- HbA1c, Vitamin D, B12, Iron studies\n"
            "- Cancer markers (PSA, CA-125, CEA, AFP)\n"
            "- COVID-19 tests (RT-PCR and Antigen)\n\n"
            "Microbiology:\n"
            "- Cultures and sensitivity testing (urine, blood, sputum, wound)\n"
            "- Stool examination\n\n"
            "Radiology:\n"
            "- Digital X-Ray\n"
            "- Ultrasound and Color Doppler\n"
            "- CT Scan (16-slice, 64-slice)\n"
            "- MRI (1.5 Tesla)\n"
            "- Mammography\n"
            "- DEXA Scan (Bone Density)\n\n"
            "Home Collection Service:\n"
            "- Available for blood and urine samples\n"
            "- Home collection hours: 6:00 AM to 10:00 AM daily\n"
            "- Booking required: Call 040-99887744 by 9:00 PM the previous day\n"
            "- Home collection charges: Rs.100 per visit (waived for senior citizens above 70)\n\n"
            "Report Delivery:\n"
            "- Routine reports: within 24 to 48 hours\n"
            "- Urgent reports: within 4 to 6 hours (extra charges apply)\n"
            "- Online report download: Available through the hospital's patient portal\n"
            "- Reports are sent via SMS/email upon request\n\n"
            "Lab Contact: 040-99887744"
        ),
    },
    {
        "id": "doc_011",
        "topic": "Health Packages",
        "text": (
            "MediCare General Hospital — Preventive Health Check-up Packages\n\n"
            "MediCare General Hospital offers affordable comprehensive health check-up packages "
            "designed for early detection and preventive care.\n\n"
            "Available Health Packages:\n\n"
            "1. Full Body Checkup Package — Rs.2,500\n"
            "   Includes 60+ tests:\n"
            "   - CBC, Blood Sugar (fasting and post-prandial), Lipid Profile\n"
            "   - Liver Function Tests, Kidney Function Tests\n"
            "   - Thyroid Function Tests (T3, T4, TSH)\n"
            "   - Urine routine and microscopy\n"
            "   - Chest X-Ray, ECG\n"
            "   - Vitamin D, Vitamin B12\n"
            "   - Doctor consultation included\n"
            "   - Validity: 30 days from booking\n\n"
            "2. Cardiac Package — Rs.4,500\n"
            "   Comprehensive cardiac health assessment:\n"
            "   - ECG (Electrocardiogram)\n"
            "   - 2D Echocardiography (Echo)\n"
            "   - Lipid Profile (Total Cholesterol, HDL, LDL, Triglycerides)\n"
            "   - Stress Test (TMT — Treadmill Test)\n"
            "   - Cardiologist consultation included\n"
            "   - Validity: 30 days from booking\n\n"
            "3. Diabetes Management Package — Rs.1,800\n"
            "   Complete diabetes screening:\n"
            "   - HbA1c (3-month blood sugar average)\n"
            "   - Fasting Blood Sugar (FBS)\n"
            "   - Post-prandial Blood Sugar (PPBS)\n"
            "   - Kidney Function Tests (Creatinine, eGFR)\n"
            "   - Urine Microalbumin (kidney damage screening)\n"
            "   - Fundus examination (eye check for diabetic retinopathy)\n"
            "   - Diabetologist consultation included\n\n"
            "4. Women's Health Package — Rs.3,200\n"
            "   Comprehensive women's health screening:\n"
            "   - CBC, Thyroid Function Tests, Vitamin D, B12, Iron studies\n"
            "   - Pap Smear\n"
            "   - Mammography\n"
            "   - Pelvic Ultrasound\n"
            "   - Bone Density (DEXA) Scan\n"
            "   - Gynecologist consultation included\n\n"
            "Packages are available Monday to Saturday. "
            "To book a package, call 040-99887766 or visit the registration counter."
        ),
    },
    {
        "id": "doc_012",
        "topic": "Hospital General Information",
        "text": (
            "MediCare General Hospital — General Information\n\n"
            "MediCare General Hospital is a premier 350-bed multi-specialty hospital located in the heart "
            "of Hyderabad, serving patients across Telangana and surrounding regions.\n\n"
            "Hospital Address:\n"
            "Plot 45, Road No. 12, Banjara Hills,\n"
            "Hyderabad — 500034, Telangana, India\n\n"
            "Contact Information:\n"
            "- Main Helpline: 040-99887766\n"
            "- Emergency (24/7): 040-12345678\n"
            "- Pharmacy: 040-99887755\n"
            "- Diagnostic Lab: 040-99887744\n\n"
            "Visiting Hours:\n"
            "- Morning: 10:00 AM to 12:00 PM\n"
            "- Evening: 5:00 PM to 7:00 PM\n"
            "- ICU patients: Special visiting as per ICU team guidance\n"
            "- NICU: Parents only, restricted entry\n\n"
            "Facilities and Amenities:\n"
            "- Parking: Free basement parking available for patients and attendants (capacity: 200 vehicles)\n"
            "- Canteen: Open 7:00 AM to 10:00 PM daily, serves Indian meals, snacks, and beverages\n"
            "- Wi-Fi: Free Wi-Fi available throughout the hospital (network: MediCare_Guest, no password)\n"
            "- ATM: SBI ATM located in the hospital lobby\n"
            "- Pharmacy: 24/7 in-house pharmacy (Ground Floor)\n"
            "- Patient Lounge: Comfortable waiting areas on every floor\n"
            "- Wheelchair and stretcher: Available at the entrance free of charge\n\n"
            "Key Departments:\n"
            "Cardiology, Orthopedics, Neurology, Pediatrics, General Medicine, Gynecology, Dermatology, "
            "ENT, Ophthalmology, Psychiatry, Urology, Gastroenterology, Nephrology, Oncology, Pulmonology\n\n"
            "Hospital certifications: NABH accredited, NABL-accredited laboratory, ISO 9001:2015 certified.\n\n"
            "For all inquiries, call: 040-99887766."
        ),
    },
]


def build_knowledge_base():
    """Build ChromaDB collection with all 12 documents. Returns (embedder, collection)."""
    from sentence_transformers import SentenceTransformer
    import chromadb

    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    client = chromadb.Client()

    # Remove existing collection if present
    try:
        client.delete_collection("medicare_kb")
    except Exception:
        pass

    collection = client.create_collection("medicare_kb")

    texts = [doc["text"] for doc in DOCUMENTS]
    ids = [doc["id"] for doc in DOCUMENTS]
    metadatas = [{"topic": doc["topic"]} for doc in DOCUMENTS]

    # Always convert NumPy array to Python list for ChromaDB
    embeddings = embedder.encode(texts).tolist()

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=texts,
        metadatas=metadatas,
    )

    print(f"✅ Knowledge base built: {len(DOCUMENTS)} documents loaded into ChromaDB collection 'medicare_kb'")
    return embedder, collection


def run_retrieval_test(embedder=None, collection=None):
    """Test retrieval for 5 sample questions. Builds KB if not provided."""
    if embedder is None or collection is None:
        embedder, collection = build_knowledge_base()

    test_questions = [
        "What time does cardiology OPD open?",
        "How much does a specialist consultation cost?",
        "Does MediCare accept Star Health insurance?",
        "What is the emergency contact number?",
        "How do I book an appointment?",
    ]

    print("\n🔍 Running Retrieval Test...")
    print("=" * 60)
    all_passed = True

    for q in test_questions:
        embedding = embedder.encode([q]).tolist()
        results = collection.query(query_embeddings=embedding, n_results=3)
        topics = [m["topic"] for m in results["metadatas"][0]]
        print(f"Q: {q}")
        print(f"   Retrieved topics: {topics}")
        print()

    print("✅ Retrieval test completed successfully!")
    return embedder, collection


if __name__ == "__main__":
    run_retrieval_test()
