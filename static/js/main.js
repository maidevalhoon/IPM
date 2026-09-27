/**
 * Granica × IIT Guwahati Hackathon
 * AI-Augmented Triage Layer (IPM Section)
 * Frontend Interactions & Multimodal Orchestrator
 * STRICT MONOCHROME EDITION: Powered by Google Gemini Multimodal API
 */

document.addEventListener('DOMContentLoaded', () => {
  // Form Input Elements
  const demoPills = document.querySelectorAll('.demo-pill-btn');
  const hostelSelect = document.getElementById('hostelSelect');
  const roomInput = document.getElementById('roomInput');
  const originalCategorySelect = document.getElementById('originalCategorySelect');
  const rawTextInput = document.getElementById('rawTextInput');
  const charCount = document.getElementById('charCount');
  const dropzone = document.getElementById('dropzone');
  const imageFileInput = document.getElementById('imageFileInput');
  const imageUrlInput = document.getElementById('imageUrlInput');
  const imageBase64Input = document.getElementById('imageBase64Input');
  const imagePreviewContainer = document.getElementById('imagePreviewContainer');
  const dropzoneEmpty = document.getElementById('dropzoneEmpty');
  const imagePreview = document.getElementById('imagePreview');
  const removeImageBtn = document.getElementById('removeImageBtn');
  const expandImageBtn = document.getElementById('expandImageBtn');
  const runTriageBtn = document.getElementById('runTriageBtn');
  const btnSpinner = document.getElementById('btnSpinner');
  const triageBtnText = document.getElementById('triageBtnText');
  const clearFormBtn = document.getElementById('clearFormBtn');
  const voiceSimBtn = document.getElementById('voiceSimBtn');

  // Output Elements & Empty State
  const emptyTriagePlaceholder = document.getElementById('emptyTriagePlaceholder');
  const triageOutput = document.getElementById('triageOutput');
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

  // State
  let currentTriageData = null;
  let activeAudioUtterance = null;
  let isPlayingAudio = false;

  // LocalStorage Settings - Default to Gemini API
  const savedApiKey = localStorage.getItem('ipm_gemini_api_key') || '';
  const savedMode = localStorage.getItem('ipm_engine_mode') || 'gemini';
  geminiApiKeyInput.value = savedApiKey;
  if (savedMode === 'smart') {
    modeSmart.checked = true;
  } else {
    modeGemini.checked = true;
  }

  // Update Character Counter
  function updateCharCount() {
    if (rawTextInput && charCount) {
      charCount.textContent = rawTextInput.value.length;
    }
  }
  rawTextInput.addEventListener('input', updateCharCount);
  updateCharCount();

  // Toast System - Strictly Monochrome
  function showToast(message, type = 'info') {
    const container = document.getElementById('toastContainer');
    const toast = document.createElement('div');
    toast.className = 'toast';
    const tag = type === 'success' ? '[OK]' : type === 'warn' ? '[!]' : '[i]';
    toast.innerHTML = `<span>${tag}</span><span>${message}</span>`;
    container.appendChild(toast);
    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      setTimeout(() => toast.remove(), 250);
    }, 2800);
  }

  // Render Triage Output into Right Pane
  function renderTriageOutput(data, studentCategory = null) {
    currentTriageData = data;
    const cat = studentCategory || originalCategorySelect.value;

    // Show triageOutput and hide placeholder
    if (emptyTriagePlaceholder) emptyTriagePlaceholder.style.display = 'none';
    if (triageOutput) triageOutput.style.display = 'flex';

    // 1. Validity Banner
    if (!data.ipm_validity) {
      validityBanner.classList.add('banner-invalid');
      validityIcon.textContent = '[NOT IPM]';
      validityTitle.textContent = 'NOT IPM SECTION PART';
      validityDesc.textContent = data.technical_summary_english;
      validityBadge.textContent = 'OUT OF SCOPE';
      dispatchNowBtn.querySelector('span').textContent = 'Submit to ' + data.corrected_department;
    } else {
      validityBanner.classList.remove('banner-invalid');
      validityIcon.textContent = '[VALID]';
      validityTitle.textContent = 'IPM VALID JURISDICTION';
      validityDesc.textContent = 'Physical campus asset verified under IPM civil/electrical maintenance scope.';
      validityBadge.textContent = 'VALID IPM';
      dispatchNowBtn.querySelector('span').textContent = 'Dispatch Work Order to ' + (data.corrected_department || 'Technician');
    }

    // 2. Department Reclassification
    displayOriginalDept.textContent = cat;
    displayCorrectedDept.textContent = data.corrected_department;

    if (cat.trim().toLowerCase() !== data.corrected_department.trim().toLowerCase()) {
      deptStatusFlag.innerHTML = '<span class="correction-tag corrected">[RECLASSIFIED BY AI]</span>';
    } else {
      deptStatusFlag.innerHTML = '<span class="correction-tag verified">[VERIFIED MATCH]</span>';
    }

    // 3. Severity Scale & Meter
    const sev = Math.max(1, Math.min(5, data.severity_score || 3));
    sevNumber.textContent = sev;
    
    const sevLabels = {
      1: 'Level 1 · Low Priority / Administrative Forwarding / Painting',
      2: 'Level 2 · Routine Minor Repair',
      3: 'Level 3 · Standard Maintenance Needed',
      4: 'Level 4 · Suspended on Live Wires / Electrical Hazard',
      5: 'Level 5 · Active Emergency / Live Current Shock Hazard'
    };
    sevDescription.textContent = sevLabels[sev] || `Level ${sev}`;

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
      chronicTitle.textContent = '[CHRONIC FAILURE DETECTED]';
      chronicDesc.textContent = 'Repeated breakdown history confirmed. Structural remedy & asset replacement mandated.';
    } else {
      chronicCard.classList.remove('chronic-alert');
      chronicTitle.textContent = 'Single Occurrence';
      chronicDesc.textContent = 'Standard single-visit maintenance workflow approved.';
    }

    // 5. Multi-Trade Interdependency
    if (data.interdependency_flag && data.interdependency_flag.trim().toLowerCase() !== 'none') {
      interdependencyCard.style.display = 'flex';
      interdependencyText.textContent = data.interdependency_flag;

      const flagLower = data.interdependency_flag.toLowerCase();
      if (flagLower.includes('phase') || flagLower.includes('before') || flagLower.includes('civil') || flagLower.includes('gap')) {
        sequenceSteps.innerHTML = `
          <div class="seq-node">Phase 1: Civil Masonry (Fill Gap in Wall & Patch)</div>
          <div class="seq-arrow">-&gt; Setting / Curing -&gt;</div>
          <div class="seq-node">Phase 2: Electrical Works (Remount Lamp & Wire)</div>
        `;
      } else {
        sequenceSteps.innerHTML = `<div class="seq-node">Inter-Department Routing / Verification</div>`;
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

    // 7. Situational Technical Summary (English)
    technicalSummaryText.textContent = data.technical_summary_english || 'No technical summary generated.';

    // 8. Assamese Directive (অসমীয়া)
    assameseText.textContent = data.technician_instructions_assamese || 'নিৰ্দেশনা উপলব্ধ নহয়।';
  }

  // Trigger Triage Pipeline Request (Using Gemini API)
  async function executeTriage() {
    const rawText = rawTextInput.value.trim();
    if (!rawText) {
      showToast('Please enter complaint details first.', 'warn');
      rawTextInput.focus();
      return;
    }

    btnSpinner.style.display = 'inline-block';
    triageBtnText.textContent = 'Gemini Multimodal Analyzing...';
    runTriageBtn.disabled = true;

    try {
      const isGeminiMode = modeGemini.checked;
      const apiKey = geminiApiKeyInput.value.trim();

      const payload = {
        raw_text: rawText,
        hostel: hostelSelect.value,
        room: roomInput.value.trim(),
        original_category: originalCategorySelect.value,
        image_url: imageUrlInput.value || null,
        image_base64: imageBase64Input.value || null,
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
        showToast('Gemini Multimodal Triage generated successfully.', 'success');
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

          imageBase64Input.value = '';

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

          // Immediately render Gemini expected output
          renderTriageOutput(t.expected_output, t.original_category);
          showToast(`Loaded: ${t.id}`, 'info');
        }
      } catch (e) {
        console.error('Error fetching demo:', e);
      }
    });
  });

  // Image File Upload and Base64 Conversion
  function processSelectedFile(file) {
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (e) => {
      const base64Data = e.target.result;
      imagePreview.src = base64Data;
      imageBase64Input.value = base64Data;
      imageUrlInput.value = ''; // Local upload overrides static URL
      imagePreviewContainer.style.display = 'block';
      dropzoneEmpty.style.display = 'none';
      showToast('Photo evidence attached.', 'success');
    };
    reader.readAsDataURL(file);
  }

  dropzone.addEventListener('click', (e) => {
    if (e.target.id === 'removeImageBtn' || e.target.id === 'expandImageBtn') return;
    if (imagePreviewContainer.style.display === 'none') {
      imageFileInput.click();
    }
  });

  imageFileInput.addEventListener('change', () => {
    if (imageFileInput.files && imageFileInput.files[0]) {
      processSelectedFile(imageFileInput.files[0]);
    }
  });

  removeImageBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    imagePreview.src = '';
    imageUrlInput.value = '';
    imageBase64Input.value = '';
    imageFileInput.value = '';
    imagePreviewContainer.style.display = 'none';
    dropzoneEmpty.style.display = 'flex';
    showToast('Photo evidence removed.', 'info');
  });

  if (expandImageBtn) {
    expandImageBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (imagePreview.src) {
        window.open(imagePreview.src, '_blank');
      }
    });
  }

  // Drag and Drop
  dropzone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropzone.style.background = '#eeeeee';
  });
  dropzone.addEventListener('dragleave', () => {
    dropzone.style.background = '';
  });
  dropzone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropzone.style.background = '';
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      imageFileInput.files = e.dataTransfer.files;
      processSelectedFile(e.dataTransfer.files[0]);
    }
  });

  // Voice Note Simulation
  voiceSimBtn.addEventListener('click', () => {
    const samples = [
      "broken thing.",
      "paint the wall",
      "Connecting laptop with lan shows no internet",
      "no table and chair in my hostel room",
      "plaster chipping off and graffiti on wall"
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
    }, 20);
  });

  // Clear Form (Resets both Form and Response sides to empty state)
  clearFormBtn.addEventListener('click', () => {
    rawTextInput.value = '';
    updateCharCount();
    roomInput.value = '';
    imagePreview.src = '';
    imageUrlInput.value = '';
    imageBase64Input.value = '';
    imageFileInput.value = '';
    imagePreviewContainer.style.display = 'none';
    dropzoneEmpty.style.display = 'flex';

    // Clear response side and deselect all demo pills
    if (emptyTriagePlaceholder) emptyTriagePlaceholder.style.display = 'flex';
    if (triageOutput) triageOutput.style.display = 'none';
    demoPills.forEach(p => p.classList.remove('active'));
    currentTriageData = null;

    showToast('Form and response cleared to blank state.', 'info');
  });

  // Assamese Audio Readout
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

  // Copy JSON Output
  copyJsonBtn.addEventListener('click', () => {
    if (!currentTriageData) return;
    navigator.clipboard.writeText(JSON.stringify(currentTriageData, null, 2)).then(() => {
      showToast('Structured JSON copied to clipboard.', 'success');
    });
  });

  // Dispatch Now Trigger
  dispatchNowBtn.addEventListener('click', () => {
    if (currentTriageData && !currentTriageData.ipm_validity) {
      showToast(`Complaint submitted to external portal: ${currentTriageData.corrected_department}`, 'info');
    } else {
      const orderNo = 'IPM-WO-' + Math.floor(100000 + Math.random() * 900000);
      showToast(`Work order ${orderNo} dispatched to frontline contractor!`, 'success');
    }
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

    const slipInterBox = document.getElementById('slipInterdependencyBox');
    const slipInterText = document.getElementById('slipInterdependency');
    if (currentTriageData.interdependency_flag && currentTriageData.interdependency_flag.trim().toLowerCase() !== 'none') {
      if (slipInterBox) slipInterBox.style.display = 'block';
      if (slipInterText) slipInterText.textContent = currentTriageData.interdependency_flag;
    } else {
      if (slipInterBox) slipInterBox.style.display = 'none';
    }

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
    showToast('Configuration saved.', 'success');
  });

  // Close modals on backdrop click
  window.addEventListener('click', (e) => {
    if (e.target === printModal) printModal.style.display = 'none';
    if (e.target === settingsModal) settingsModal.style.display = 'none';
  });

  // Initialize Page Mode
  const isBlankPage = document.body.getAttribute('data-is-blank') === 'true' ||
                      window.location.pathname === '/new' ||
                      window.location.search.includes('blank=');

  if (!isBlankPage) {
    const firstPill = document.querySelector('.demo-pill-btn.active');
    if (firstPill) {
      firstPill.click();
    }
  } else {
    // Blank Mode: Both form and response sides are clean empty states
    if (emptyTriagePlaceholder) emptyTriagePlaceholder.style.display = 'flex';
    if (triageOutput) triageOutput.style.display = 'none';
    demoPills.forEach(p => p.classList.remove('active'));
    currentTriageData = null;
  }
});
