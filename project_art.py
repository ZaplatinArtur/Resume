"""Original monochrome scenes for the project gallery and case backgrounds."""

SCENES = {
    'tokens': '''<g stroke="currentColor" stroke-width="1.4">
      <g opacity=".25"><path d="M40 65h205m-205 45h205m-205 45h205m-205 45h205m-205 45h205"/><path d="M55 42v221m45-221v221m45-221v221m45-221v221m45-221v221"/></g>
      <g class="semantic-points"><circle cx="72" cy="82" r="8"/><circle cx="105" cy="132" r="8"/><circle cx="157" cy="95" r="8"/><circle cx="195" cy="167" r="8"/><circle cx="137" cy="211" r="8"/><path d="M72 82l85 13 38 72-58 44-32-79-33-50m33 50 52-37m-52 37 90 35"/></g>
      <path class="signal-path" d="M252 150h57m-14-13 14 13-14 13"/>
      <g class="token-stream"><rect x="330" y="72" width="67" height="62" rx="3"/><rect x="409" y="72" width="67" height="62" rx="3"/><rect x="488" y="72" width="67" height="62" rx="3"/><path d="M344 94h37m-37 15h20m47 67h134m-134 18h103m-103 18h124"/><rect x="330" y="162" width="55" height="70" rx="3"/><path d="M343 182h29m-29 14h21m-21 14h26"/></g>
      </g><g fill="currentColor"><text x="45" y="32">SEMANTIC SPACE</text><text x="330" y="47">SID / CODEBOOK</text><text x="44" y="289">EMBEDDINGS → TOKENS → RECOMMENDATIONS</text><text x="344" y="254">TERM IDS</text></g>''',
    'scales': '''<g stroke="currentColor" stroke-width="1.5">
      <path d="M40 226h245v44H40Zm11-6h223v6m-139 18h56v18h-56Z"/>
      <g class="fruit-item fruit-apple"><path d="M148 117c-43-37-78 4-56 59 13 35 35 28 54 25 19 3 41 10 54-25 22-55-13-96-52-59Z"/><path d="M148 116c-4-27 17-34 29-32-2 19-15 27-29 24"/></g>
      <g class="fruit-item fruit-pear"><path d="M144 97c-22 0-19 41-32 59-29 39-12 56 33 56s62-17 33-56c-13-18-10-59-34-59Z"/><path d="M145 98V75m0 7c13-10 24-4 25 4-15 7-18 4-25-4"/></g>
      <g class="fruit-item fruit-tomato"><circle cx="147" cy="166" r="46"/><path d="M147 128l-20-9 7 17-19 9 24 1 8 13 8-13 24-1-19-9 7-17-20 9Zm0-6v-18"/></g>
      <path d="M73 99v-9h19m117 0h17v9M73 193v14h19m117 0h17v-14" opacity=".5"/>
      <path class="scale-scan" d="M78 128h144" stroke-width="2"/>
      <path class="signal-path" d="M294 168h64m-13-12 13 12-13 12"/>
      <rect x="381" y="77" width="150" height="176" rx="4"/><path d="M397 106h114m-114 17h68m-68 35h34m-34 17h83m-83 17h101m-101 17h54M411 237h89"/>
      </g><g fill="currentColor"><text x="91" y="54">VISUAL RECOGNITION</text><text x="400" y="63">PRODUCT CATALOG</text><text x="139" y="257" font-size="8">KG</text><text x="73" y="292">64 VARIETIES / IMAGE + WEIGHT</text></g>''',
    'search': '''<g stroke="currentColor" stroke-width="1.4">
      <rect x="38" y="55" width="166" height="182" rx="4"/><path d="M48 70h20m-20 0v20m145-20h-20m20 0v20M48 222h20m-20 0v-20m145 20h-20m20 0v-20"/>
      <path d="M101 88h29v31l19 24v64H82v-64l19-24Z"/><rect class="detection-box" x="77" y="79" width="76" height="132" stroke-dasharray="4 4"/><path d="M92 155h45m-45 14h34m-34 14h45"/>
      <path class="signal-path" d="M220 148h63m-15-13 15 13-15 13"/>
      <g class="catalog-grid"><rect x="316" y="57" width="73" height="81"/><rect x="399" y="57" width="73" height="81"/><rect x="482" y="57" width="73" height="81"/><rect x="316" y="149" width="73" height="81"/><rect x="399" y="149" width="73" height="81"/><rect x="482" y="149" width="73" height="81"/>
      <path d="M340 73h19v14l10 14v24h-40v-24l11-14Zm76 3h39v48h-39Zm83 8h39v37h-39Zm-157 82h19v16l10 13v23h-40v-23l11-13Zm75 8h39v41h-39Zm81 1h40v42h-40Z"/></g>
      <rect class="catalog-hit" x="314" y="147" width="77" height="85" stroke-width="3"/><path class="catalog-hit" d="M366 216l8 8 16-19"/>
      </g><g fill="currentColor"><text x="43" y="39">PHOTO / LABEL</text><text x="318" y="39">2 102 PRODUCTS</text><text x="42" y="279">YOLO → SIGLIP2 + TEXT → RRF</text></g>''',
    'wine': '''<g stroke="currentColor" stroke-width="1.5">
      <path d="M113 41h31v75l25 34v112H89V150l24-34Z"/><path d="M109 46h39m-38 15h37M110 83h37"/><rect x="98" y="164" width="62" height="70" rx="2"/><path d="M109 202h40m-40 11h31m-31 10h40"/>
      <path class="ocr-scan" d="M81 157h99" stroke-width="2"/><path class="signal-path" d="M192 194h84m-14-13 14 13-14 13"/>
      <rect x="295" y="74" width="248" height="161" rx="3"/><path d="M310 96h217m-217 81h216m-216 26h164" opacity=".5"/>
      <path class="ocr-type" d="M315 132v25h16v-25m10 0v25m11 0v-25l18 25v-25m11 0h20v25h-20Z" stroke-width="2"/>
      <g class="match-check"><circle cx="496" cy="204" r="15"/><path d="M487 204l6 6 12-14"/></g>
      </g><g fill="currentColor"><text x="107" y="192" font-size="9">VINO</text><text x="307" y="61">OCR / CATALOG MATCH</text><text x="313" y="223" font-size="8">MATCH · REVIEW · NOT_IN_CATALOG</text></g>''',
    'detection': '''<g class="terrain-lines" stroke="currentColor" opacity=".25"><path d="M-100 79c160 84 227-94 385-16s247 64 415-10M-100 104c160 84 227-94 385-16s247 64 415-10M-100 129c160 84 227-94 385-16s247 64 415-10M-100 154c160 84 227-94 385-16s247 64 415-10M-100 179c160 84 227-94 385-16s247 64 415-10M-100 204c160 84 227-94 385-16s247 64 415-10M-100 229c160 84 227-94 385-16s247 64 415-10"/></g>
      <g stroke="currentColor" stroke-width="1.4"><path d="M16 20h35m-35 0v35m568-35h-35m35 0v35M16 281h35m-35 0v-35m568 35h-35m35 0v-35"/>
      <g class="deer-herd"><path d="M166 153l28-6 27 8-8 17h-34l-13-19m8 17-9 26m21-25-3 24m26-24 11 24m-2-36 10-24 8 4-8 17m4-19 4-20m-4 11-11-7m14 4 10-11"/><path d="M321 202l24-7 24 8-9 15h-31l-8-16m8 14-7 24m17-23-3 23m21-24 9 24m-2-37 11-20 8 4-8 15m5-19v-18m0 8-9-6m10 4 9-8"/></g>
      <rect class="detection-box" x="149" y="105" width="102" height="104" stroke-dasharray="4 4"/><rect class="detection-box detection-delay" x="305" y="158" width="92" height="93" stroke-dasharray="4 4"/>
      <g class="drone"><rect x="407" y="53" width="23" height="23" rx="3"/><path d="M410 56l-15-15m32 15 15-15m-32 32-15 15m32-15 15 15"/><circle cx="390" cy="36" r="12"/><circle cx="447" cy="36" r="12"/><circle cx="390" cy="93" r="12"/><circle cx="447" cy="93" r="12"/></g>
      </g><g fill="currentColor"><text x="67" y="36">UAV / AERIAL DETECTION</text><text x="70" y="272">DETECT → TRACK → COUNT</text></g>''',
    'text': '''<g stroke="currentColor" stroke-width="1.4">
      <rect x="50" y="37" width="193" height="227"/><path d="M68 63h143m-143 9h89" stroke-width="2"/>
      <g class="document-lines"><path d="M68 98h69m-69 12h66m-66 12h69m-69 12h61m-61 12h68m-68 12h69m-69 12h53m-53 12h68m-68 12h69m-69 12h58m-58 12h64m-64 12h59M151 98h71m-71 12h65m-65 12h70m-70 12h61m-61 12h68m-68 12h71m-71 12h66m-66 12h63m-63 12h71m-71 12h61m-61 12h68m-68 12h60"/></g>
      <path class="signal-path" d="M263 150h63m-13-13 13 13-13 13"/>
      <rect x="348" y="70" width="204" height="156"/><path d="M365 97h141" stroke-width="2"/>
      <path class="summary-line" d="M365 124h148m-148 24h123m-123 24h140" stroke-width="2"/>
      <path d="M375 248h151m-75-6v12" opacity=".6"/>
      <circle class="sentiment-dot" cx="457" cy="248" r="5" fill="currentColor"/>
      </g><g fill="currentColor"><text x="52" y="25">ARTICLE / COMMENTS</text><text x="351" y="58">SUMMARY</text><text x="379" y="282">SENTIMENT ANALYSIS</text></g>''',
    'market': '''<g stroke="currentColor" stroke-width="1.3">
      <g opacity=".2"><path d="M39 50h290m-290 44h290m-290 44h290m-290 44h290m-290 44h290M50 36v205m53-205v205m53-205v205m53-205v205m53-205v205m53-205v205"/></g>
      <path d="M50 231h279V38"/>
      <path class="market-signal" pathLength="100" d="M53 202l32-18 23 17 37-65 29 25 28-34 25 19 34-71 29 26 33-52" stroke-width="2.5"/>
      <g class="market-candles" opacity=".5"><path d="M67 155v57m41-70v65m39-89v61m39-93v64m39-76v71m39-91v64"/><path d="M63 169h8v24h-8Zm41-13h8v35h-8Zm39-20h8v28h-8Zm39-32h8v29h-8Zm39-12h8v30h-8Zm39-23h8v32h-8Z"/></g>
      <circle cx="435" cy="136" r="52"/><circle class="decision-ring" cx="435" cy="136" r="69" stroke-dasharray="3 8"/><path class="signal-path" d="M334 136h45m108 0h65v111H435v-54m-12 14 12-14 12 14"/>
      </g><g fill="currentColor"><text x="404" y="142">AGENT</text><text x="52" y="273">TEST MARKET / STATE → ACTION → REVIEW</text><text x="405" y="33">DECISION LOOP</text></g>''',
}


def scene_body(kind):
    return SCENES[kind]
