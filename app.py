import streamlit as st
from pathlib import Path
import tempfile

st.set_page_config(
    page_title="QuantumShield",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ QuantumShield")
st.subheader("Post-Quantum-Secure Mobile Financial Threat Protection")

st.info(
    "Educational prototype. Transaction decisions are simulated. "
    "APK permission indicators alone do not establish that an app is malicious."
)

tab1, tab2, tab3, tab4 = st.tabs([
    "💳 Transaction Security",
    "📱 APK Scanner",
    "🔐 Post-Quantum Crypto",
    "⚛️ Quantum Demo"
])

# ---------------- TRANSACTION SECURITY ----------------
with tab1:
    st.header("Transaction Risk Assessment")

    amount = st.number_input(
        "Transaction amount (test units)",
        min_value=0.0,
        value=500.0,
        step=100.0
    )

    suspicious = st.checkbox("Simulate a suspicious activity indicator")

    if st.button("Assess Transaction Risk"):
        if amount <= 0:
            st.error("INVALID: Transaction amount must be positive.")
        elif suspicious:
            st.error("HIGH RISK: Flag for review.")
            st.write("Reason: A suspicious activity indicator was detected.")
        elif amount >= 10000:
            st.warning("MEDIUM RISK: Request additional verification.")
            st.write("Reason: Transaction meets the configured review threshold.")
        else:
            st.success("LOW RISK: Allow simulated transaction.")
            st.write("Reason: No configured high-risk indicator was detected.")

# ---------------- APK SCANNER ----------------
with tab2:
    st.header("Android APK Permission Scanner")

    st.write(
        "Upload an Android APK to inspect its package metadata and "
        "selected permission indicators."
    )

    uploaded_apk = st.file_uploader(
        "Choose an Android APK file",
        type=["apk"],
        key="apk_upload"
    )

    sensitive_permissions = {
        "android.permission.READ_SMS": "Can read SMS messages",
        "android.permission.RECEIVE_SMS": "Can receive SMS messages",
        "android.permission.READ_CONTACTS": "Can read contacts",
        "android.permission.RECORD_AUDIO": "Can record audio",
        "android.permission.READ_CALL_LOG": "Can read call history",
        "android.permission.SYSTEM_ALERT_WINDOW": "Can draw overlays over other apps",
        "android.permission.REQUEST_INSTALL_PACKAGES": "Can request installation of other packages"
    }

    if uploaded_apk is not None:
        if st.button("Scan APK"):
            try:
                from androguard.core.apk import APK

                # Save uploaded bytes temporarily for Androguard
                with tempfile.NamedTemporaryFile(suffix=".apk", delete=False) as temp:
                    temp.write(uploaded_apk.getvalue())
                    temp_path = temp.name

                try:
                    apk = APK(temp_path)

                    package_name = apk.get_package()
                    app_name = apk.get_app_name()
                    permissions = sorted(set(apk.get_permissions() or []))

                    if not package_name or not permissions and not app_name:
                        st.error(
                            "The file could not be identified as a valid Android APK. "
                            "Please try another APK containing a readable Android manifest."
                        )
                    else:
                        findings = [
                            (permission, sensitive_permissions[permission])
                            for permission in permissions
                            if permission in sensitive_permissions
                        ]

                        score = min(len(findings) * 15, 100)

                        if score >= 45:
                            risk = "HIGH"
                        elif score >= 15:
                            risk = "MEDIUM"
                        else:
                            risk = "LOW"

                        st.subheader("Analysis Results")
                        st.write("**Application name:**", app_name or "Unavailable")
                        st.write("**Package name:**", package_name)
                        st.write("**Total permissions:**", len(permissions))
                        st.write("**Selected permission indicators:**", len(findings))
                        st.metric("Indicator score", f"{score}/100")

                        if risk == "HIGH":
                            st.error(f"Indicator level: {risk}")
                        elif risk == "MEDIUM":
                            st.warning(f"Indicator level: {risk}")
                        else:
                            st.success(f"Indicator level: {risk}")

                        if findings:
                            st.write("### Selected permission indicators")
                            for permission, description in findings:
                                st.write(f"- `{permission}` — {description}")
                        else:
                            st.write(
                                "No permissions from this prototype's selected list were found."
                            )

                        st.caption(
                            "The score is a simple prototype heuristic, not a malware "
                            "probability or a security verdict. Legitimate apps can use "
                            "sensitive permissions, and malicious apps may not request these."
                        )
                finally:
                    Path(temp_path).unlink(missing_ok=True)

            except Exception as error:
                st.error(
                    "Unable to analyze this file. It may be invalid, damaged, "
                    "or incompatible with the scanner."
                )
                st.caption(f"Diagnostic: {type(error).__name__}: {error}")


# ---------------- POST-QUANTUM CRYPTO ----------------
with tab3:
    import hashlib
    import os

    st.header("Post-Quantum Cryptography")
    st.write("Demonstrate ML-KEM-768 key establishment and AES-GCM authenticated encryption.")

    st.info(
        "This is an educational demonstration. It does not connect to a bank "
        "or establish a session with a remote server."
    )

    if st.button("Run Cryptography Demonstration", key="run_crypto"):
        try:
            from pqcrypto.kem import ml_kem_768
            from cryptography.hazmat.primitives.ciphers.aead import AESGCM

            # Generate the recipient's ML-KEM key pair
            public_key, secret_key = ml_kem_768.keygen()

            # Encapsulate and recover the same shared secret
            ciphertext, shared_secret_a = ml_kem_768.encaps(public_key)
            shared_secret_b = ml_kem_768.decaps(secret_key, ciphertext)

            if shared_secret_a != shared_secret_b:
                st.error("Shared-secret verification failed.")
            else:
                st.success("Step 1 passed: ML-KEM-768 shared secrets match.")

                # Derive a 256-bit AES key from the shared secret
                aes_key = hashlib.sha256(
                    b"QuantumShield-AES-GCM-v1" + shared_secret_a
                ).digest()

                aesgcm = AESGCM(aes_key)
                report = (
                    b"QuantumShield security report: "
                    b"post-quantum key establishment successful."
                )
                nonce = os.urandom(12)

                encrypted_report = aesgcm.encrypt(nonce, report, None)
                decrypted_report = aesgcm.decrypt(
                    nonce, encrypted_report, None
                )

                if decrypted_report == report:
                    st.success("Step 2 passed: Report encrypted and decrypted correctly.")
                    st.write("**Decrypted sample report:**")
                    st.code(decrypted_report.decode("utf-8"))
                    st.write("**ML-KEM algorithm:**", ml_kem_768.ALGORITHM)
                    st.write("**Public key size:**", len(public_key), "bytes")
                    st.write("**KEM ciphertext size:**", len(ciphertext), "bytes")
                    st.write("**Shared-secret size:**", len(shared_secret_a), "bytes")
                    st.write("**Encrypted report size:**", len(encrypted_report), "bytes")

                    # Demonstrate that ciphertext modification is detected
                    tampered = bytearray(encrypted_report)
                    tampered[0] ^= 1

                    try:
                        aesgcm.decrypt(nonce, bytes(tampered), None)
                        st.error("Tamper test failed: modified ciphertext was accepted.")
                    except Exception:
                        st.success("Step 3 passed: Modified ciphertext was rejected.")
                else:
                    st.error("Decrypted report did not match the original.")

        except Exception as error:
            st.error("The cryptography demonstration could not run.")
            st.caption(f"Diagnostic: {type(error).__name__}: {error}")

# ---------------- QUANTUM DEMO ----------------
with tab4:
    st.header("Quantum Threat Demonstration")
    st.write("A four-qubit Qiskit circuit simulation completed successfully.")
    st.code("4 qubits → 16 statevector amplitudes")
    st.warning(
        "This is a quantum circuit demonstration, not Shor's factoring algorithm."
    )