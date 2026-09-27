/**
 * Granica × IIT Guwahati Hackathon
 * AI-Augmented Triage Layer (IPM Section)
 * Frontend Interactions & Triage Orchestrator
 */

document.addEventListener('DOMContentLoaded', () => {
  // DOM Elements
  const demoPills = document.querySelectorAll('.demo-pill-btn');
  const hostelSelect = document.getElementById('hostelSelect');
  const roomInput = document.getElementById('roomInput');
  const originalCategorySelect = document.getElementById('originalCategorySelect');
  const rawTextInput = document.getElementById('rawTextInput');
  const charCount = document.getElementById('charCount');
  const dropzone = document.getElementById('dropzone');
  const imageFileInput = document.getElementById('imageFileInput');
  const imageUrlInput = document.getElementById('imageUrlInput');
  const imagePreviewContainer = document.getElementById('imagePreviewContainer');
  const dropzoneEmpty = document.getElementById('dropzoneEmpty');
  const imagePreview = document.getElementById('imagePreview');
  const removeImageBtn = document.getElementById('removeImageBtn');
  const runTriageBtn = document.getElementById('runTriageBtn');
  const btnSpinner = document.getElementById('btnSpinner');
  const triageBtnText = document.getElementById('triageBtnText');
  const clearFormBtn = document.getElementById('clearFormBtn');
  const voiceSimBtn = document.getElementById('voiceSimBtn');

  // Output Elements
  const validityBanner = document.getElementById('validityBanner');
  const validityIcon = document.getElementById('validityIcon');
  const validityTitle = document.getElementById('validityTitle');
  const validityDesc = document.getElementById('validityDesc');
  const validityBadge = document.getElementById('validityBadge');
  
  const displayOriginalDept = document.getElementById('displayOriginalDept');
  const displayCorrectedDept = document.getElementById('displayCorrectedDept');
  const deptStatusFlag = document.getElementById('deptStatusFlag');

  const sevNumber = document.getElementById('sevNumber');
  const sevDescription = document.getElementById('sevDescription');
  const sevSegments = document.querySelectorAll('.sev-seg');

  const chronicCard = document.getElementById('chronicCard');
  const chronicStatus = document.getElementById('chronicStatus');
  const chronicTitle = document.getElementById('chronicTitle');
  const chronicDesc = document.getElementById('chronicDesc');

  const interdependencyCard = document.getElementById('interdependencyCard');
  const interdependencyText = document.getElementById('interdependencyText');
  const sequenceSteps = document.getElementById('sequenceSteps');

  const toolsList = document.getElementById('toolsList');
  const technicalSummaryText = document.getElementById('technicalSummaryText');
  const assameseText = document.getElementById('assameseText');
  const playAudioBtn = document.getElementById('playAudioBtn');
  const audioBtnText = document.getElementById('audioBtnText');
  const copyAssameseBtn = document.getElementById('copyAssameseBtn');
  const copyJsonBtn = document.getElementById('copyJsonBtn');
  const dispatchNowBtn = document.getElementById('dispatchNowBtn');

  // Modals & Settings
  const printSlipBtn = document.getElementById('printSlipBtn');
  const printModal = document.getElementById('printModal');
  const closePrintModalBtn = document.getElementById('closePrintModalBtn');
  const triggerPrintBtn = document.getElementById('triggerPrintBtn');

  const openSettingsBtn = document.getElementById('openSettingsBtn');
  const settingsModal = document.getElementById('settingsModal');
  const closeSettingsModalBtn = document.getElementById('closeSettingsModalBtn');
  const saveSettingsBtn = document.getElementById('saveSettingsBtn');
  const geminiApiKeyInput = document.getElementById('geminiApiKeyInput');
  const modeSmart = document.getElementById('modeSmart');
  const modeGemini = document.getElementById('modeGemini');

  // Application State
  let currentTriageData = null;
  let activeAudioUtterance = null;
  let isPlayingAudio = false;

  // Load Saved Settings from LocalStorage
  const savedApiKey = localStorage.getItem('ipm_gemini_api_key') || '';
  const savedMode = localStorage.getItem('ipm_engine_mode') || 'smart';
  geminiApiKeyInput.value = savedApiKey;
  if (savedMode === 'gemini') {
    modeGemini.checked = true;
  } else {
    modeSmart.checked = true;
  }

  // Update Character Counter
  function updateCharCount() {
    if (rawTextInput && charCount) {
      charCount.textContent = rawTextInput.value.length;
    }
  }
  rawTextInput.addEventListener('input', updateCharCount);
  updateCharCount();

  // Toast System
  function showToast(message, type = 'info') {
    const container = document.getElementById('toastContainer');
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerHTML = `<span>${type === 'success' ? '✅' : type === 'warn' ? '⚠️' : 'ℹ️'}</span><span>${message}</span>`;
    container.appendChild(toast);
    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      setTimeout(() => toast.remove(), 300);
    }, 3200);
  }

  // Render Triage Output into Right Pane
  function renderTriageOutput(data, studentCategory = null) {
    currentTriageData = data;
    const cat = studentCategory || originalCategorySelect.value;

    // 1. Validity Banner
    if (!data.ipm_validity) {
      validityBanner.classList.add('banner-invalid');
      validityIcon.textContent = '❌';
      validityTitle.textContent = 'INVALID FOR IPM · RE-ROUTED TO COMPUTER CENTER (CC)';
      validityDesc.textContent = 'Issue pertains to campus LAN / IT connectivity. IPM physical civil/electrical triage rejected; auto-transferred to Computer Center network desk.';
      validityBadge.textContent = 'Out of Scope';
    } else {
      validityBanner.classList.remove('banner-invalid');
      validityIcon.textContent = '✅';
      validityTitle.textContent = 'IPM Valid Jurisdiction';
      validityDesc.textContent = 'Physical campus asset verified under IPM civil/electrical maintenance scope.';
      validityBadge.textContent = 'Valid IPM';
    }

    // 2. Department Reclassification
    displayOriginalDept.textContent = cat;
    displayCorrectedDept.textContent = data.corrected_department;

    if (cat.trim().toLowerCase() !== data.corrected_department.trim().toLowerCase()) {
      deptStatusFlag.innerHTML = '<span class="correction-tag corrected">⚠️ Reclassified by AI</span>';
    } else {
      deptStatusFlag.innerHTML = '<span class="correction-tag verified">✓ Verified Match</span>';
    }

    // 3. Severity Scale & Meter
    const sev = Math.max(1, Math.min(5, data.severity_score || 3));
    sevNumber.textContent = sev;
    
    const sevLabels = {
      1: 'Level 1 · Minor Cosmetic Issue',
      2: 'Level 2 · Routine Minor Repair',
      3: 'Level 3 · Standard Maintenance Needed',
      4: 'Level 4 · Severe Operational Hazard',
      5: 'Level 5 · Active Emergency / Water Leak Flooding'
    };
    sevDescription.textContent = sevLabels[sev];

    sevSegments.forEach(seg => {
      const level = parseInt(seg.getAttribute('data-level'), 10);
      if (level <= sev) {
        seg.classList.add('active');
      } else {
        seg.classList.remove('active');
      }
    });

    // 4. Chronic Issue Flag
    if (data.chronic_issue_flag) {
      chronicCard.classList.add('chronic-alert');
      chronicTitle.textContent = '⚠️ CHRONIC FAILURE DETECTED';
      chronicDesc.textContent = 'Text specifies repeated unresolved breakdowns (e.g. "4th time"). Mandate: Full asset replacement unit (Disallow temporary repair).';
    } else {
      chronicCard.classList.remove('chronic-alert');
      chronicTitle.textContent = 'Single Occurrence';
      chronicDesc.textContent = 'Standard single-visit maintenance workflow approved.';
    }

    // 5. Multi-Trade Interdependency
    if (data.interdependency_flag && data.interdependency_flag.trim().toLowerCase() !== 'none') {
      interdependencyCard.style.display = 'flex';
      interdependencyText.textContent = data.interdependency_flag;

      // Render step pills if masonry / split ticket
      if (data.interdependency_flag.toLowerCase().includes('before')) {
        sequenceSteps.innerHTML = `
          <div class="seq-node">Phase 1: Civil Works (Masonry Patching)</div>
          <div class="seq-arrow">➔ 24h Cure ➔</div>
          <div class="seq-node">Phase 2: Carpentry Mounting</div>
        `;
      } else if (data.interdependency_flag.toLowerCase().includes('split')) {
        sequenceSteps.innerHTML = `
          <div class="seq-node">Trade A: Plumbing (Fixture Fix)</div>
          <div class="seq-arrow">&</div>
          <div class="seq-node">Trade B: Carpentry (Door Latch)</div>
        `;
      } else {
        sequenceSteps.innerHTML = `<div class="seq-node">Multi-Department Coordinated Action</div>`;
      }
    } else {
      interdependencyCard.style.display = 'none';
    }

    // 6. Predicted Tools & Hardware Checklist
    toolsList.innerHTML = '';
    const tools = data.predicted_tools_parts || [];
    if (tools.length === 0) {
      toolsList.innerHTML = '<li class="tool-item">No physical tools required for this request.</li>';
    } else {
      tools.forEach(tool => {
        const li = document.createElement('li');
        li.className = 'tool-item';
        li.innerHTML = `
          <input type="checkbox" class="tool-checkbox" checked>
          <span>${tool}</span>
        `;
        toolsList.appendChild(li);
      });
    }

    // 7. Technical Summary (English)
    technicalSummaryText.textContent = data.technical_summary_english || 'No technical summary generated.';

    // 8. Assamese Directive (অসমীয়া)
    assameseText.textContent = data.technician_instructions_assamese || 'নিৰ্দেশনা উপলব্ধ নহয়।';
  }

  // Trigger Triage Pipeline Request
  async function executeTriage() {
    const rawText = rawTextInput.value.trim();
    if (!rawText) {
      showToast('Please enter complaint details first.', 'warn');
      rawTextInput.focus();
      return;
    }

    btnSpinner.style.display = 'inline-block';
    triageBtnText.textContent = 'Analyzing Physical Evidence...';
    runTriageBtn.disabled = true;

    try {
      const isGeminiMode = modeGemini.checked;
      const apiKey = geminiApiKeyInput.value.trim();

      const payload = {
        raw_text: rawText,
        hostel: hostelSelect.value,
        room: roomInput.value.trim(),
        original_category: originalCategorySelect.value,
        image_url: imageUrlInput.value,
        api_key: apiKey || null,
        force_offline: !isGeminiMode
      };

      const response = await fetch('/api/triage', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      const resJson = await response.json();
      if (resJson.status === 'success') {
        renderTriageOutput(resJson.data, originalCategorySelect.value);
        showToast('AI Triage completed successfully!', 'success');
      } else {
        showToast(resJson.message || 'Triage processing error.', 'warn');
      }
    } catch (err) {
      console.error(err);
      showToast('Network error during triage execution.', 'warn');
    } finally {
      btnSpinner.style.display = 'none';
      triageBtnText.textContent = 'Run AI Triage & Augmentation';
      runTriageBtn.disabled = false;
    }
  }

  runTriageBtn.addEventListener('click', executeTriage);

  // Demo Pills Carousel Click Handling
  demoPills.forEach(pill => {
    pill.addEventListener('click', async () => {
      demoPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');

      const ticketId = pill.getAttribute('data-ticket-id');
      try {
        const res = await fetch(`/api/demos/${ticketId}`);
        const data = await res.json();
        if (data.status === 'success' && data.ticket) {
          const t = data.ticket;
          hostelSelect.value = t.hostel;
          roomInput.value = t.room;
          originalCategorySelect.value = t.original_category;
          rawTextInput.value = t.raw_text;
          updateCharCount();

          if (t.image_url) {
            imagePreview.src = t.image_url;
            imageUrlInput.value = t.image_url;
            imagePreviewContainer.style.display = 'block';
            dropzoneEmpty.style.display = 'none';
          } else {
            imagePreviewContainer.style.display = 'none';
            dropzoneEmpty.style.display = 'flex';
            imageUrlInput.value = '';
          }

          // Immediately render expected output
          renderTriageOutput(t.expected_output, t.original_category);
          showToast(`Loaded demo: ${t.id} (${t.title})`, 'info');
        }
      } catch (e) {
        console.error('Error fetching demo:', e);
      }
    });
  });

  // Image Dropzone Handling
  dropzone.addEventListener('click', (e) => {
    if (e.target.id === 'removeImageBtn' || e.target.id === 'expandImageBtn') return;
    if (imagePreviewContainer.style.display === 'none') {
      imageFileInput.click();
    }
  });

  imageFileInput.addEventListener('change', () => {
    if (imageFileInput.files && imageFileInput.files[0]) {
      const file = imageFileInput.files[0];
      const reader = new FileReader();
      reader.onload = (e) => {
        imagePreview.src = e.target.result;
        imageUrlInput.value = ''; // Local upload
        imagePreviewContainer.style.display = 'block';
        dropzoneEmpty.style.display = 'none';
        showToast('Photo evidence attached.', 'success');
      };
      reader.readAsDataURL(file);
    }
  });

  removeImageBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    imagePreview.src = '';
    imageUrlInput.value = '';
    imageFileInput.value = '';
    imagePreviewContainer.style.display = 'none';
    dropzoneEmpty.style.display = 'flex';
  });

  // Drag and Drop
  dropzone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropzone.style.borderColor = 'var(--accent-cyan)';
  });
  dropzone.addEventListener('dragleave', () => {
    dropzone.style.borderColor = '';
  });
  dropzone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropzone.style.borderColor = '';
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      imageFileInput.files = e.dataTransfer.files;
      const event = new Event('change');
      imageFileInput.dispatchEvent(event);
    }
  });

  // Voice Note Simulation
  voiceSimBtn.addEventListener('click', () => {
    const samples = [
      "Room 274 ke paas ke water cooler ki pipe me leakage ho gya he , baar baar kuch beep beep noise ata rehta hai usse...",
      "Connecting laptop with lan shows no internet. Ethernet port yellow light blinking continuously, tried 3 cables.",
      "My fan is creating very noise like it will come down and this is 4 th time when I am posting complaint!",
      "Windows are not opening properly, jammed tight in monsoon and also there is no handle in the windows"
    ];
    const picked = samples[Math.floor(Math.random() * samples.length)];
    rawTextInput.value = '';
    let i = 0;
    const interval = setInterval(() => {
      rawTextInput.value += picked[i];
      i++;
      updateCharCount();
      if (i >= picked.length) {
        clearInterval(interval);
        showToast('Voice transcription simulated.', 'success');
      }
    }, 25);
  });

  // Clear Form
  clearFormBtn.addEventListener('click', () => {
    rawTextInput.value = '';
    updateCharCount();
    roomInput.value = '';
    imagePreview.src = '';
    imageUrlInput.value = '';
    imageFileInput.value = '';
    imagePreviewContainer.style.display = 'none';
    dropzoneEmpty.style.display = 'flex';
    showToast('Form cleared.', 'info');
  });

  // Assamese Audio Readout (Web Speech API)
  playAudioBtn.addEventListener('click', () => {
    if (!('speechSynthesis' in window)) {
      showToast('Browser does not support Speech Synthesis audio.', 'warn');
      return;
    }

    if (isPlayingAudio) {
      window.speechSynthesis.cancel();
      isPlayingAudio = false;
      playAudioBtn.classList.remove('playing');
      audioBtnText.textContent = 'Play Audio';
      return;
    }

    const textToRead = assameseText.textContent.trim();
    if (!textToRead) return;

    activeAudioUtterance = new SpeechSynthesisUtterance(textToRead);
    // Bengali/Assamese locale code
    activeAudioUtterance.lang = 'bn-IN';
    activeAudioUtterance.rate = 0.95;

    activeAudioUtterance.onstart = () => {
      isPlayingAudio = true;
      playAudioBtn.classList.add('playing');
      audioBtnText.textContent = 'Stop Audio';
    };

    activeAudioUtterance.onend = () => {
      isPlayingAudio = false;
      playAudioBtn.classList.remove('playing');
      audioBtnText.textContent = 'Play Audio';
    };

    activeAudioUtterance.onerror = () => {
      isPlayingAudio = false;
      playAudioBtn.classList.remove('playing');
      audioBtnText.textContent = 'Play Audio';
    };

    window.speechSynthesis.speak(activeAudioUtterance);
  });

  // Copy Assamese Text
  copyAssameseBtn.addEventListener('click', () => {
    navigator.clipboard.writeText(assameseText.textContent.trim()).then(() => {
      showToast('Assamese directive copied to clipboard.', 'success');
    });
  });

  // Copy JSON Schema
  copyJsonBtn.addEventListener('click', () => {
    if (!currentTriageData) return;
    navigator.clipboard.writeText(JSON.stringify(currentTriageData, null, 2)).then(() => {
      showToast('JSON schema copied to clipboard.', 'success');
    });
  });

  // Dispatch Now Trigger
  dispatchNowBtn.addEventListener('click', () => {
    const orderNo = 'IPM-WO-' + Math.floor(100000 + Math.random() * 900000);
    showToast(`Work order ${orderNo} dispatched to frontline contractor!`, 'success');
  });

  // Printable Slip Modal
  printSlipBtn.addEventListener('click', () => {
    if (!currentTriageData) return;
    document.getElementById('slipHostel').textContent = hostelSelect.value;
    document.getElementById('slipRoom').textContent = roomInput.value;
    document.getElementById('slipDept').textContent = currentTriageData.corrected_department;
    document.getElementById('slipSeverity').textContent = `Level ${currentTriageData.severity_score}`;
    document.getElementById('slipSummary').textContent = currentTriageData.technical_summary_english;
    document.getElementById('slipAssamese').textContent = currentTriageData.technician_instructions_assamese;

    const slipTools = document.getElementById('slipTools');
    slipTools.innerHTML = '';
    (currentTriageData.predicted_tools_parts || []).forEach(t => {
      const li = document.createElement('li');
      li.textContent = t;
      slipTools.appendChild(li);
    });

    printModal.style.display = 'flex';
  });

  closePrintModalBtn.addEventListener('click', () => {
    printModal.style.display = 'none';
  });

  triggerPrintBtn.addEventListener('click', () => {
    window.print();
  });

  // Settings Modal
  openSettingsBtn.addEventListener('click', () => {
    settingsModal.style.display = 'flex';
  });

  closeSettingsModalBtn.addEventListener('click', () => {
    settingsModal.style.display = 'none';
  });

  saveSettingsBtn.addEventListener('click', () => {
    localStorage.setItem('ipm_gemini_api_key', geminiApiKeyInput.value.trim());
    localStorage.setItem('ipm_engine_mode', modeGemini.checked ? 'gemini' : 'smart');
    settingsModal.style.display = 'none';
    showToast('Engine settings saved.', 'success');
  });

  // Close modals on backdrop click
  window.addEventListener('click', (e) => {
    if (e.target === printModal) printModal.style.display = 'none';
    if (e.target === settingsModal) settingsModal.style.display = 'none';
  });

  // Initialize with First Demo Ticket
  const firstPill = document.querySelector('.demo-pill-btn.active');
  if (firstPill) {
    firstPill.click();
  }
});
