# raw_element 校對報告

- Source: `01_notes/精華筆記/raw_element.md`
- Total Q/A rows: 520
- OK: 366
- 修正: 104
- 疑義: 17
- 缺答案: 33

## Worker 統計

| Worker output | OK | 修正 | 疑義 | 缺答案 | Total |
|---|---:|---:|---:|---:|---:|
| `agent_A_segments_01_09.md` | 61 | 13 | 1 | 1 | 76 |
| `agent_B_segments_10_18.md` | 68 | 28 | 4 | 1 | 101 |
| `agent_C_segments_19_24.md` | 43 | 12 | 1 | 3 | 59 |
| `agent_D_segments_25_31.md` | 54 | 14 | 3 | 4 | 75 |
| `agent_E_segments_32_40.md` | 69 | 19 | 3 | 16 | 107 |
| `agent_F_segments_41_49.md` | 71 | 18 | 5 | 8 | 102 |

## 優先處理清單

- 先處理 `缺答案`：這些多半是 PDF 複製漏頁、原文寫「下頁」或答案段落被截斷。
- 再處理 `疑義`：多半是 guideline/地區/考古語境問題，建議回查原題或當年教材。
- `修正` 已在整理答案中給較安全版本，但若要併入正式筆記，仍應再做一次主筆記風格蒸餾。

## 需校對或已修正題目

| ID | 狀態 | 題目 | 整理答案 | 原始行號 | 校對註記 | Worker |
|---|---|---|---|---|---|---|
| S01-Q05 | 修正 | 跟 Hodgkin lymphoma 有關的是哪一種 HPV？ | 不是 HPV；Hodgkin lymphoma 主要與 EBV（Epstein-Barr virus）有關。 | Q: 0011; A: 0033-0035 | 原文寫 HPV 6，會誤導；HPV 6 是低風險型，主要與生殖器疣相關。 | `agent_A_segments_01_09.md` |
| S03-Q11 | 修正 | Aneurysm rupture 後預防 vasospasm 的 3H？ | Hypervolemia、hypertension、hemodilution。 | Q: 0147-0149; A: 0151 | 原文 `Hemodilusion` 拼字錯，修為 hemodilution。 | `agent_A_segments_01_09.md` |
| S04-Q06 | 修正 | 列舉三類可能造成 delirium 的藥物。 | Anticholinergics（抗膽鹼藥，如 atropine）、opioid/narcotic analgesics（鴉片類止痛藥）、BZD（benzodiazepine）。 | Q: 0171; A: 0211-0213 | 原文 `Nacrotic` 拼字錯；整理為 opioid/narcotic。 | `agent_A_segments_01_09.md` |
| S05-Q07 | 修正 | 高血鈣治療中最快的是？幾小時內作用的是？ | 最快整體可用 hemodialysis（重症/腎衰竭時）；一般急性處置先 IV normal saline，最快降鈣藥是 calcitonin（約 4-6 小時），bisphosphonate 需 2-4 天。 | Q: 0229; A: 0259-0261 | 原文未列 calcitonin，且把 glucocorticoid 列為小時級易誤導；loop diuretic 只在補液後容量過多時考慮。 | `agent_A_segments_01_09.md` |
| S05-Q08 | 修正 | 惡性腫瘤相關高血鈣與 vitamin D 過多各建議用什麼？ | Malignancy hypercalcemia：IV bisphosphonate（如 zoledronic acid/pamidronate）或 denosumab；症狀嚴重可短期加 calcitonin。Vitamin D 過多或 calcitriol-mediated 高血鈣：glucocorticoid。 | Q: 0231; A: 0263-0267 | 原文把 glucocorticoid 放在惡性腫瘤相關治療內，需限縮到 vitamin D/calcitriol-mediated 或 lymphoma 情境。 | `agent_A_segments_01_09.md` |
| S06-Q02 | 疑義 | Primary aldosteronism 的尿液 pH 應更酸或更鹼？ | 需回查考古題原文：原文答尿偏鹼；但醛固酮與低血鉀會增加 H+ 分泌，臨床可見酸性尿/paradoxical aciduria。 | Q: 0273; A: 0303-0311 | 原文「尿液 pH 變鹼」與常見生理說法不完全一致，建議整合時回查 101-1-(三)-46。 | `agent_A_segments_01_09.md` |
| S06-Q07 | 修正 | 疑似高醛固酮、未確診時，哪些降壓藥避免？通常用什麼？ | 檢查 ARR 前盡量停會干擾 RAAS 的藥：ACEi/ARB、利尿劑/MRA、beta-blocker 等；可改 alpha-blocker、verapamil SR 或 hydralazine。 | Q: 0287-0289; A: 0325-0329 | 原文只寫 alpha blocker 或 CCB；整理時補上 verapamil SR/少干擾藥，避免把所有 CCB 當等價。 | `agent_A_segments_01_09.md` |
| S07-Q04 | 修正 | HFpEF 中原本四本柱剩下誰有效？ | HFpEF：SGLT2 inhibitor 最穩，主要降低 HF hospitalization/複合心衰事件；MRA 可在部分族群降低住院。死亡率不宜寫成已明確下降。 | Q: 0361; A: 0393-0395 | 原文寫 SGLT2i 可降低死亡率，過度肯定；主要證據是降低心衰住院/複合終點。 | `agent_A_segments_01_09.md` |
| S07-Q05 | 修正 | 心衰竭 beta-blocker 中實證有效的三種？ | Carvedilol、bisoprolol、metoprolol succinate。 | Q: 0363; A: 0397-0399 | 原文只寫 metoprolol；HFrEF 實證需記 succinate，不是 tartrate。 | `agent_A_segments_01_09.md` |
| S07-Q08 | 修正 | Pulsus alternans、electrical alternans、pulsus paradoxus 各是什麼？誰與左心衰最相關？ | Pulsus alternans：搏動強弱交替，最連結 severe LV dysfunction/left HF。Electrical alternans：QRS 振幅交替，想到大量心包膜積液/心包填塞。Pulsus paradoxus：吸氣 SBP 下降 >10 mmHg，想到 cardiac tamponade、severe asthma/COPD 等。 | Q: 0369-0371; A: 0407-0415 | 原文 `cardial tamponade` 拼字修為 cardiac tamponade；SVC obstruction 非高頻核心鑑別。 | `agent_A_segments_01_09.md` |
| S07-Q09 | 修正 | NYHA 分級背一次；NYHA 是跟誰比？ | I：日常活動不受限；II：日常活動才有症狀；III：低於日常活動即有症狀；IV：休息也有症狀。NYHA 是看 ordinary physical activity（日常活動限制），不是跟病人自己巔峰體能比較。 | Q: 0373; A: 0417-0421 | 原文「跟原本的自己比」會誤導。 | `agent_A_segments_01_09.md` |
| S08-Q02 | 修正 | Long QT syndrome 與 Brugada syndrome 各是哪個離子通道問題？ | Long QT syndrome 常考 K+ channel；LQT3 是 Na+ channel。Brugada syndrome 常考 SCN5A Na+ channel。 | Q: 0427; A: 0441-0443 | 原文旁註「LQTS-3 是 Na+ 跟 Ca2+」不精確；Ca2+ 是少見亞型如 Timothy syndrome。 | `agent_A_segments_01_09.md` |
| S08-Q04 | 修正 | 會造成 QT prolong 的 antiarrhythmic 與抗生素？ | Antiarrhythmic：class IA（quinidine、procainamide、disopyramide）與 class III（sotalol、dofetilide、ibutilide、amiodarone）。抗生素：macrolides、fluoroquinolones。 | Q: 0431-0433; A: 0447-0451 | 原文抗生素只列 fluoroquinolone，漏 macrolide。 | `agent_A_segments_01_09.md` |
| S09-Q06 | 修正 | 肺栓塞的心雜音特色？ | Pulmonary embolism 可有 P2 亢進；若造成肺高壓/肺動脈瓣逆流，可聽 Graham Steell murmur。 | Q: 0487; A: 0513-0515 | 原文寫 `DVT`，題目是肺栓塞；Graham Steell 是肺高壓造成的肺動脈瓣逆流雜音，不是每個 PE 都有。 | `agent_A_segments_01_09.md` |
| S09-Q12 | 缺答案 | Paradoxical S2 splitting 的鑑別診斷？ | 已可整理：A2 延遲造成 paradoxical splitting，如 AS、LBBB、HOCM；特色是呼氣分裂、吸氣變窄/消失。 | Q: 0497; A: 0539-0542 | 原文在 0542 截斷於「呼氣時」，後半答案缺漏；肺動脈提早關閉分支需回查來源。 | `agent_A_segments_01_09.md` |
| S10-Q01 | 修正 | UC 與 Crohn 之中，切掉盲腸/闌尾可預防哪個？ | UC：appendectomy（闌尾切除）有保護效果；Crohn 反而可視為風險相關。 | Q: 543-545; A: 581-583 | 原文答 UC 可用，但題目「切掉盲腸」應理解為闌尾切除。 | `agent_B_segments_10_18.md` |
| S10-Q05 | 修正 | 哪個 IBD 跟癌症有關？ | UC 與 colorectal cancer 關聯最典型；Crohn colitis 也會增加 colorectal cancer 風險。 | Q: 553; A: 591 | 原文只寫 UC，容易誤會 Crohn 完全無癌症風險。 | `agent_B_segments_10_18.md` |
| S10-Q11 | 修正 | GERD、肥胖、男性、achalasia、酗酒分別偏哪種食道癌？ | GERD、肥胖、Barrett esophagus 偏腺癌；achalasia、酗酒偏 SCC；男性兩者皆為風險但腺癌更典型。 | Q: 565-567; A: 601 | 原文把男性只放腺癌，考試可接受但需避免誤會男性只影響腺癌。 | `agent_B_segments_10_18.md` |
| S10-Q13 | 疑義 | 食道癌流病中 SCC 與腺癌哪個多？ | 全球與台灣常記 SCC 較多；西方國家腺癌比例已上升且可較常見。 | Q: 571; A: 607 | 原文「SCC比例較多」需看地區與考題語境。 | `agent_B_segments_10_18.md` |
| S10-Q14 | 修正 | 食道癌 T1, T2, T3, T4a, T4b 分別侵犯到哪裡？ | T1：lamina propria/muscularis mucosa/submucosa；T2：muscularis propria；T3：adventitia；T4a：可切除鄰近構造如 pleura、pericardium、diaphragm；T4b：不可切除如 aorta、vertebral body、trachea。 | Q: 573; A: 609-613 | 原文 T1 只寫 submucosa，補完整層次；T4a/T4b 原文方向可用。 | `agent_B_segments_10_18.md` |
| S10-Q16 | 疑義 | 食道癌 TNM 中 T/N 多少以上保底 stage III？ | 不建議硬背單一保底；stage grouping 受組織型、grade、位置影響。可考向：T4 或 N2/N3 屬 locally advanced、高 stage。 | Q: 577; A: 619 | 原文「T4a 或 N2 以上保底 IIIB」過度簡化，整合時需確認採用的 AJCC 版次。 | `agent_B_segments_10_18.md` |
| S10-Q17 | 疑義 | 什麼條件下食道癌建議先 neoadjuvant CCRT 再手術？ | 最穩考法：locally advanced resectable，尤其 T3/T4a 或 N+；部分教材也把 T2 以上列入。 | Q: 579; A: 621 | 原文「T2以上或 N+」偏考試簡化；臨床上 cT2N0 是否 neoadjuvant 有爭議。 | `agent_B_segments_10_18.md` |
| S11-Q03 | 修正 | 抽菸、老年、高油高糖、燒烤、H. pylori、咖啡、適量酒精，哪些是胰臟癌風險？ | 高產值記：抽菸、老年、肥胖/高熱量飲食、慢性胰臟炎、糖尿病、家族史。咖啡與適量酒精不是典型風險；H. pylori 證據較弱。 | Q: 629-631; A: 669 | 原文把高油高糖、燒烤列風險可作考題記憶，但臨床高產值應改成肥胖/高熱量飲食。 | `agent_B_segments_10_18.md` |
| S11-Q05 | 修正 | BRCA2、STK11、PRSS1/SPINK1、MMR 基因增加胰臟癌機率排序？ | 粗略風險：STK11（Peutz-Jeghers）最高；PRSS1 hereditary pancreatitis 也高；Lynch/MMR 與 BRCA2 較低。 | Q: 635-639; A: 673-677 | 原文排序方向可用；`SPIN11` 疑為 `SPINK1` 或與 `PRSS1` 混寫，需修正基因名。 | `agent_B_segments_10_18.md` |
| S11-Q06 | 修正 | 胰臟癌做 Whipple 的禁忌症？ | 遠端轉移如肝、腹膜；SMA/celiac/common hepatic artery 明顯侵犯；或無法重建的 SMV/portal vein 侵犯。 | Q: 641-643; A: 679-683 | 原文把 SMV/portal vein 任何侵犯都列禁忌；現行概念是可重建靜脈侵犯不一定絕對禁忌。 | `agent_B_segments_10_18.md` |
| S11-Q09 | 修正 | Courvoisier sign 是什麼？跟什麼病有關或無關？ | Painless jaundice 加上 palpable distended gallbladder；提示胰臟頭部/壺腹周邊惡性阻塞，不像膽結石。 | Q: 649; A: 689-691 | 原文只寫右上腹無痛腫塊，需補 jaundice 與 distended gallbladder。 | `agent_B_segments_10_18.md` |
| S11-Q13 | 修正 | 胰臟癌 high-risk factor 三個？ | 若指 IPMN/胰臟囊性病灶 high-risk stigmata：阻塞性黃疸、main pancreatic duct ≥10 mm、enhancing mural nodule ≥5 mm。 | Q: 657; A: 699-703 | 原文答案其實是 IPMN high-risk stigmata，不是一般胰臟癌 risk factor；cutoff 建議用 ≥。 | `agent_B_segments_10_18.md` |
| S12-Q02 | 疑義 | 哪兩種肝炎病毒不會周產期感染？ | 考試二分法：HAV、HEV 以 fecal-oral 為主，不列常見周產期感染；HBV、HCV 可周產期感染。 | Q: 709; A: 749-751 | HEV 孕期垂直傳播有報告；若國考用典型傳染途徑，答案仍多抓 HAV/HEV。 | `agent_B_segments_10_18.md` |
| S12-Q05 | 修正 | 急性 B 肝多少比例變慢性？ | 成人急性 HBV 約 <5% 變慢性；新生兒感染慢性化比例很高。 | Q: 715; A: 757 | 原文 5% 是成人概念；兒童/新生兒不能套用。 | `agent_B_segments_10_18.md` |
| S12-Q07 | 修正 | HBV 與 HCV 最常見傳染途徑？ | HBV：高盛行區常見周產期/垂直傳染；HCV：血液暴露，尤其注射藥物、輸血/醫療暴露。 | Q: 719; A: 761 | 原文說 B、C 都最常見垂直傳染；HCV 這點錯，會影響作答。 | `agent_B_segments_10_18.md` |
| S12-Q10 | 修正 | 媽媽有 HBV 或 HCV 能哺乳嗎？ | HBV：新生兒完成 HBIG 與疫苗後可哺乳；HCV：通常可哺乳，但乳頭破裂流血時暫停。 | Q: 725; A: 767-769 | 原文 HCV「正常哺乳」需補 cracked/bleeding nipple 例外。 | `agent_B_segments_10_18.md` |
| S12-Q11 | 修正 | 母親 HBV viral load 低於多少，垂直感染率才低？ | 常用門檻：HBV DNA <200,000 IU/mL；約等於 <10^6 copies/mL。 | Q: 727; A: 771 | 原文只寫 10^6，需補單位避免 IU/mL 與 copies/mL 混淆。 | `agent_B_segments_10_18.md` |
| S12-Q12 | 修正 | 母親 HBsAg 陽性，新生兒出生後怎麼處理？ | 出生後越快越好，12 小時內給 HBV vaccine + HBIG，分不同部位注射。 | Q: 729; A: 773-775 | 原文寫 24 小時內；許多指引用 12 小時內，考試取更嚴格。 | `agent_B_segments_10_18.md` |
| S13-Q04 | 修正 | HBV DNA level 會在哪些 phase 驗不到？ | 不活化期 HBV DNA 低或可測不到；resolved infection 血中通常測不到；occult infection 血中可低/陰性但肝內仍有 HBV DNA。 | Q: 807; A: 823-825 | 原文把不活化期與 occult 直接寫「驗不到」過度絕對。 | `agent_B_segments_10_18.md` |
| S14-Q01 | 缺答案 | Child-Pugh 有哪幾項？最低分？class B 範圍？細項數值？ | Raw 已有 5 項：bilirubin、albumin、PT/INR、ascites、hepatic encephalopathy；最低 5 分。class B 與細項 cutoff 原文未收完整。 | Q: 837-839; A: 873-877 | 原文寫「細項在下頁」，本 segment 沒有下頁內容，整合時需回查。 | `agent_B_segments_10_18.md` |
| S14-Q02 | 修正 | MELD score 用途與檢驗項目？ | 用於肝硬化死亡風險與肝移植排序；MELD-Na 主要看 bilirubin、INR、creatinine、Na。MELD 3.0 再納入 albumin、sex。 | Q: 841; A: 879-883 | 原文混入「病因」較像舊版概念；現行考向以 bili/INR/Cr/Na 為主。 | `agent_B_segments_10_18.md` |
| S14-Q07 | 修正 | 腹水 PMN 大於多少表示感染？ | PMN ≥250/mm3 支持 SBP。 | Q: 853; A: 897 | 原文寫 >250；常用診斷門檻是 ≥250。 | `agent_B_segments_10_18.md` |
| S14-Q09 | 修正 | 胃食道靜脈曲張第一線藥物、非藥物、初級預防？ | 急性出血：octreotide/terlipressin + ceftriaxone，再做 endoscopic variceal ligation；初級預防：non-selective beta blocker 或 EVL。 | Q: 859-861; A: 903-907 | 原文把 EVL 放非藥物正確；初級預防除了 NSBB，EVL 也可用於高風險或不能用 NSBB 者。 | `agent_B_segments_10_18.md` |
| S14-Q11 | 修正 | 肝腦病變怎麼診斷與治療？ | 臨床診斷；血氨不能單獨診斷或排除。Tx：lactulose，必要時加 rifaximin（利福昔明）。 | Q: 865; A: 911-913 | 原文「Rifaxime」拼字錯，應為 rifaximin。 | `agent_B_segments_10_18.md` |
| S15-Q03 | 修正 | Achalasia 最常見外科手術？ | Heller myotomy（常合併 partial fundoplication）；POEM 也是治療選項。 | Q: 927; A: 963 | 原文混入「鋇劑攝影」，那是檢查不是外科手術。 | `agent_B_segments_10_18.md` |
| S16-Q04 | 修正 | NAC、停 metformin、sodium bicarbonate、鹼化尿液、提早透析，哪個有預防效果？ | 真正有證據的預防是 isotonic IV hydration；停 metformin 是避免 AKI 後乳酸中毒，不是預防 contrast-associated AKI。 | Q: 1007-1009; A: 1037 | 原文說停 metformin 才有預防效果，會把「避免併發症」誤當「預防腎病變」。 | `agent_B_segments_10_18.md` |
| S16-Q06 | 修正 | 心導管後 AKI 兩大可能原因與鑑別？ | Contrast-associated AKI：多 24-48 小時上升、3-5 天高峰；atheroembolic renal disease：較延遲，常有 livedo reticularis、eosinophilia、低補體等。 | Q: 1013; A: 1043-1051 | 原文方向可用，補 atheroembolism 鑑別線索。 | `agent_B_segments_10_18.md` |
| S16-Q08 | 修正 | NSF 接觸後多久有症狀？像什麼病？治療？ | 多在數週後出現皮膚硬化，像 scleromyxedema/scleroderma；處理以避免 gadolinium、改善腎功能，已洗腎者暴露後可安排透析降低暴露量，但已發病無可靠特效。 | Q: 1019; A: 1055-1059 | 原文「提早洗腎有幫助」需限縮為暴露後降低 gadolinium 負荷，不能當成 NSF 特效治療。 | `agent_B_segments_10_18.md` |
| S17-Q01 | 修正 | High anion gap metabolic acidosis 鑑別講 8 個。 | GOLDMARK：Glycols（ethylene/propylene glycol）、Oxoproline（慢性 acetaminophen）、L-lactate/D-lactate、Methanol、Aspirin/salicylate、Renal failure、Ketoacidosis（DKA/酒精/飢餓）。 | Q: 1073; A: 1093-1099 | 原文重複水楊酸/阿斯匹靈，且乙醇本身不是典型 HAGMA，應改成 alcoholic ketoacidosis。 | `agent_B_segments_10_18.md` |
| S17-Q02 | 修正 | High AG 時如何知道是否合併 normal AG 酸中毒？ | 算 delta ratio：ΔAG = AG - 正常AG；ΔHCO3 = 24 - HCO3；ΔAG/ΔHCO3。<1 合併 NAGMA；1-2 單純 HAGMA；>2 合併 metabolic alkalosis。 | Q: 1075-1077; A: 1101-1117 | 原文寫 >1 即合併代謝鹼，應為 >2 較典型；1-2 可視為單純 HAGMA。 | `agent_B_segments_10_18.md` |
| S17-Q05 | 修正 | RTA 分型：Fanconi、DM nephropathy、Sjogren、腎結石、高血鉀、尿 pH、後尿道瓣膜？ | Fanconi syndrome → Type 2；DM nephropathy → Type 4；Sjogren → Type 1；腎結石 → Type 1，常為 calcium phosphate；高血鉀 → Type 4；尿 pH >5.5 → Type 1；posterior urethral valve 可造成 Type 4。 | Q: 1083-1089; A: 1129-1131 | 原文 `Faconi` 應為 Fanconi；尿 pH cutoff 常用 >5.5。 | `agent_B_segments_10_18.md` |
| S17-Q06 | 修正 | 酗酒造成 ketoacidosis 的血糖、insulin、血鉀？ | Alcoholic ketoacidosis：血糖低或正常、insulin 低；血鉀可表面正常/高，但 total body potassium 常缺乏。 | Q: 1091; A: 1133 | 原文只寫高血鉀，考試容易漏掉總體缺鉀與補液後低鉀風險。 | `agent_B_segments_10_18.md` |
| S18-Q02 | 修正 | FGF-23 上升時血鈣、血磷？ | FGF-23 主要降血磷，並抑制 1-alpha hydroxylase 使 calcitriol 下降；血鈣可下降或接近不變。 | Q: 1141; A: 1163 | 原文「降血鈣、降血磷」太簡化；FGF-23 的主軸是降磷與降 calcitriol。 | `agent_B_segments_10_18.md` |
| S19-Q05 | 修正 | MRKH 病因、無月經分類、輸卵管/子宮/陰道/卵巢/第二性徵有無，以及 type II 影響？ | MRKH（Mayer-Rokitansky-Kuster-Hauser syndrome）為 Mullerian duct 發育不全，造成原發無月經；子宮與上段陰道缺如或發育不全，卵巢與第二性徵正常；輸卵管不應一律寫無。Type II 可合併腎臟、骨骼、心臟與聽力/耳部異常。 | Q: 1205-1209; A: 1225-1231 | 原文寫輸卵管、子宮、陰道都沒有；國考主軸是子宮/上陰道缺如與卵巢正常，輸卵管可有或可異常。 | `agent_C_segments_19_24.md` |
| S20-Q05 | 修正 | Mallet finger 是什麼關節變形與什麼結構受傷？ | DIP 屈曲、無法主動伸直；terminal extensor tendon 在 DIP 附近斷裂或撕脫。 | Q: 1243; A: 1283 | 原文寫 PIP 伸直、DIP 屈曲、lateral band 斷掉；核心應是 DIP 的 terminal extensor tendon injury。 | `agent_C_segments_19_24.md` |
| S20-Q06 | 修正 | Gamekeeper thumb 是什麼關節、什麼結構斷掉，不能做什麼？ | 大拇指 MCP 的 ulnar collateral ligament 斷裂；造成 valgus 不穩，key pinch/抓握力量差。 | Q: 1245; A: 1285-1287 | 原文有 UCL 與不穩定，但未補「不能 key pinch/抓握」。 | `agent_C_segments_19_24.md` |
| S20-Q07 | 疑義 | RA 的關節外表現何者最多？眼睛病與內分泌常見問題？ | 若選項有骨質疏鬆可選為常見共病/表現；典型 extra-articular 最常考 rheumatoid nodule。眼：episcleritis/scleritis、乾眼；內分泌：hypoandrogenism。 | Q: 1247-1251; A: 1289-1291 | 原文寫 osteoporosis 最多、鞏膜炎、hypoandrogenesium；「最多」需看題目選項與定義。 | `agent_C_segments_19_24.md` |
| S21-Q02 | 缺答案 | Shigella 的腸道外併發症，除 reactive arthritis 外？ | 缺答案；原文未提供。 | Q: 1319; A: - | 醫學上常回查 seizure、HUS（hemolytic uremic syndrome，溶血尿毒症候群），但不可當作 raw 已有答案。 | `agent_C_segments_19_24.md` |
| S21-Q03 | 修正 | Campylobacter 的腸道外併發症，除 reactive arthritis 外？ | Guillain-Barre syndrome（GBS，格林-巴利症候群）最常考；也可有 bacteremia、pancreatitis 等少見併發症。 | Q: 1321; A: 1337 | 原文寫「腦膜炎、胰臟癌」；胰臟癌不對，腦膜炎不是常考主軸。 | `agent_C_segments_19_24.md` |
| S21-Q04 | 修正 | Yersinia 的腸道外併發症，除 reactive arthritis 外？ | Erythema nodosum 常考；也可有 mesenteric adenitis/pseudoappendicitis。 | Q: 1325; A: 1339 | 原文寫 hemolytic anemia，非典型常考答案。 | `agent_C_segments_19_24.md` |
| S22-Q05 | 修正 | 發炎性肌肉病變要驗哪個？ | Anti-Jo-1；特別對應 antisynthetase syndrome。 | Q: 1367; A: 1395 | 原文寫 Anti-Jo，應補 Anti-Jo-1。 | `agent_C_segments_19_24.md` |
| S23-Q01 | 修正 | 反覆鼻竇炎、生長不良加病毒/胞內菌、反覆皮膚膿瘍/口腔感染、常腦膜炎/關節炎/菌血症，各猜什麼缺陷？ | 反覆 sinopulmonary infection：B cell/抗體缺陷；failure to thrive 加病毒或胞內病原：T cell 缺陷；皮膚膿瘍與口腔感染：phagocyte/neutrophil 缺陷；腦膜炎、關節炎、菌血症：補體缺陷。 | Q: 1409-1415; A: 1451-1457 | 原文「肉芽細胞」應改為顆粒球/吞噬細胞，不是 granuloma。 | `agent_C_segments_19_24.md` |
| S23-Q08 | 修正 | 哪一種免疫缺乏會 CD19 = 0？ | Bruton agammaglobulinemia/X-linked agammaglobulinemia（BTK mutation）；B cell 幾乎缺如，CD19 = 0。 | Q: 1437; A: 1479 | 原文 agammaglobulemia 拼字錯，應為 agammaglobulinemia。 | `agent_C_segments_19_24.md` |
| S23-Q11 | 修正 | 受 Neisseria 感染，猜哪種先天免疫缺損？ | Terminal complement C5-C9 缺陷最典型；若廣泛莢膜菌感染則再想 C3 或抗體缺陷。 | Q: 1447; A: 1491-1493 | 原文只寫補體缺損且把 pneumococcus/H. influenzae 一起歸入；Neisseria 要特別指 terminal complement。 | `agent_C_segments_19_24.md` |
| S24-Q01 | 修正 | 大血管炎兩個？中血管炎一個？小血管炎五個？ | 大血管：Takayasu arteritis、giant cell arteritis。中血管：polyarteritis nodosa（PAN，結節性多動脈炎）。小血管常考：GPA、MPA、EGPA、IgA vasculitis/Henoch-Schonlein purpura、cutaneous leukocytoclastic vasculitis 或 cryoglobulinemic vasculitis。Behcet disease 應另列 variable-vessel vasculitis。 | Q: 1497-1503; A: 1499-1503 | 原文只列小血管部分且把 Behcet 放 IC 小血管；分類上 Behcet 是 variable-vessel。EPGA 為 EGPA 拼字錯。 | `agent_C_segments_19_24.md` |
| S24-Q07 | 修正 | 反覆鼻竇炎、氣喘、肢體跛行、polymyalgia rheumatica、可觸摸紫斑各對應哪個血管炎？ | 反覆鼻竇炎：GPA；氣喘：EGPA；肢體跛行：Takayasu；polymyalgia rheumatica：GCA；palpable purpura：IgA vasculitis 最典型，小血管炎如 EGPA/其他 leukocytoclastic vasculitis 也可見。 | Q: 1533-1541; A: 1535-1539 | 原文 EPGA 拼字錯；palpable purpura 非 EGPA 專一。 | `agent_C_segments_19_24.md` |
| S24-Q12 | 修正 | Henoch 的血小板數與補體？ | 血小板不變，屬 non-thrombocytopenic purpura；血清補體多正常，低補體較非典型。 | Q: 1569; A: 1575 | 原文寫補體下降；IgA vasculitis 可有組織 C3 沉積，但血清補體通常正常。 | `agent_C_segments_19_24.md` |
| S24-Q14 | 缺答案 | 鞏膜炎、表層鞏膜炎、角膜炎、視神經炎、視網膜血管炎中，哪些不是 Behcet 常見眼表現？ | 缺答案；原文未提供。 | Q: 1577-1581; A: - | 常考 Behcet 眼病灶是 uveitis 與 retinal vasculitis；本題需回查原選項，避免把少見表現硬判。 | `agent_C_segments_19_24.md` |
| S24-Q15 | 缺答案 | 病理切片看到 leukocytoclastic，診斷是什麼？ | 缺答案；推測方向是 leukocytoclastic vasculitis，若有 IgA 沉積則支持 IgA vasculitis。 | Q: 1585; A: - | 原文答案缺漏，需回查來源。 | `agent_C_segments_19_24.md` |
| S25-Q02 | 修正 | Hodgkin lymphoma 可能與哪些病毒相關？ | 國考主軸抓 EBV（Epstein-Barr virus）。 | Q: 1591; A: 1629 | 原文列 EBV、CMV、HPV6；CMV/HPV6 不是 Hodgkin 的標準必背致病關聯。 | `agent_D_segments_25_31.md` |
| S25-Q05 | 修正 | Hodgkin 與 non-Hodgkin 骨轉移偏 osteoblastic 或 osteolytic？ | Hodgkin 偏 osteoblastic；non-Hodgkin 偏 osteolytic。 | Q: 1599-1601; A: 1637-1651 | 原文寫 non-Hodgkin 是 osteoclast；應寫成 osteolytic。 | `agent_D_segments_25_31.md` |
| S25-Q10 | 缺答案 | Non-Hodgkin lymphoma 併發 cold IgM antibody，最可能是哪種自體免疫抗體？ | 原文缺答案；醫學上常考 cold agglutinin disease 為 IgM anti-I，需回查原題。 | Q: 1617-1619; A: 無 | 不把推測當作 raw 答案。 | `agent_D_segments_25_31.md` |
| S25-Q12 | 修正 | AIDS-defining 惡性腫瘤包括哪些？ | Kaposi sarcoma、特定 non-Hodgkin lymphoma（Burkitt/immunoblastic/primary CNS lymphoma）、invasive cervical cancer。 | Q: 1623; A: 1667 | 原文列肛門癌；anal cancer 是 HIV-associated cancer，但不是 AIDS-defining cancer。 | `agent_D_segments_25_31.md` |
| S26-Q04 | 缺答案 | PNH 是什麼 gene mutation？紅血球缺哪些 CD？ | 原文缺答案；醫學上為 PIGA mutation，造成 CD55/CD59 缺乏。 | Q: 1677-1679; A: 無 | raw 未提供此題答案，需回查來源。 | `agent_D_segments_25_31.md` |
| S26-Q08 | 修正 | 急性排斥 signal 1、2、3 分別是什麼？ | Signal 1：APC peptide-MHC 被 TCR/CD3 辨識；Signal 2：CD80/CD86 對 CD28 costimulation；Signal 3：IL-2 接 IL-2R，活化 mTOR 促 T cell 增生。 | Q: 1689-1701; A: 1723-1735 | 原文把 signal 1 寫成 TCR 丟 IL-2；IL-2 產生需 TCR 訊號加 costimulation。另「街上」為「接上」錯字。 | `agent_D_segments_25_31.md` |
| S28-Q01 | 疑義 | AML、ALL、CML、CLL 五年存活率排序？ | 考試粗排：CLL > CML > ALL > AML。 | Q: 1807; A: 1855 | 存活率受年齡與治療年代影響很大；兒童 ALL 例外較好。 | `agent_D_segments_25_31.md` |
| S28-Q03 | 修正 | AML 風險分類：t(15;17)、CEBPA 雙等位、del(5q)、17p、inv(16)、t(8;21)、FLT3-ITD high 哪些好、哪些差？ | Favorable：t(15;17)、CEBPA biallelic、inv(16)、t(8;21)；adverse：del(5q)、17p abnormality、FLT3-ITD high。 | Q: 1811-1815; A: 1859-1861 | 原文寫 FTL3，應為 FLT3。 | `agent_D_segments_25_31.md` |
| S28-Q06 | 修正 | 兒科 ALL 預後好/差的 cytogenetics？ | 好：t(12;21)、high hyperdiploidy、trisomy 4/10/17；差：hypodiploidy、t(9;22)、t(4;11)、11q23/KMT2A rearrangement。 | Q: 1823-1827; A: 1869-1873 | 原文把 trisomy 10 寫成 t(10;14)，且 hypodiploidy 拼字錯。 | `agent_D_segments_25_31.md` |
| S28-Q07 | 疑義 | CML 的 LAP score 升或降？還有哪些病會下降？ | CML 的 LAP score 下降；同向低分常背 PNH、aplastic anemia、pernicious anemia、hereditary hypophosphatasia。 | Q: 1831-1833; A: 1875-1879 | 原文列 TTP；不是高頻標準 LAP low 清單，建議回查原題。 | `agent_D_segments_25_31.md` |
| S28-Q11 | 修正 | Down syndrome、輻射/BCR-ABL、最常 DIC 的血癌、APL 治療、hypogammaglobulinemia 各對應？ | Down syndrome：ALL 與 AML 風險皆上升，AML 常考 AMKL/M7；BCR-ABL 多為自發體細胞突變；最常 DIC：APL；APL Tx：ATRA（all-trans retinoic acid，全反式維甲酸）合併 arsenic trioxide 或化療，並積極支持性輸血；hypogammaglobulinemia：CLL。 | Q: 1849-1853; A: 1893-1901 | 原文只寫 Down syndrome=>AML，過窄；APL 治療句尾混入 platelet transfusion，整理成 disease-specific Tx 加支持治療。 | `agent_D_segments_25_31.md` |
| S29-Q01 | 修正 | 血小板低於多少要輸？哪些病不宜常規輸血小板？ | 預防性 <10k；<20k 且感染/出血風險；<50k 且 active bleeding 或高出血風險 procedure。TTP/HUS、HIT 不常規輸 platelet，除非危及生命出血或必要處置；HELLP 不是絕對禁忌，依生產/出血需求。 | Q: 1905; A: 1941-1945 | 原文把 HELLP 也寫成絕對禁忌，會誤導臨床判斷。 | `agent_D_segments_25_31.md` |
| S29-Q07 | 缺答案 | HIT 哪一型會引起血栓？ | 原文缺答案；醫學上為 HIT type II（免疫型 anti-PF4/heparin）。 | Q: 1923; A: 無 | raw 未提供此題答案，需回查來源。 | `agent_D_segments_25_31.md` |
| S30-Q02 | 修正 | 補 vitamin K 後可改善凝血時間的黃疸，機轉是什麼？ | Obstructive/cholestatic jaundice：膽汁排出差，脂溶性 vitamin K 吸收差，補 K 可改善 prolonged PT；若不改善，想 hepatocellular failure。 | Q: 1995-1997; A: 2045-2049 | 題幹寫 thrombin time 可能錯；vitamin K 影響的是 PT/INR，不是典型 thrombin time。 | `agent_D_segments_25_31.md` |
| S30-Q04 | 缺答案 | Direct bilirubin 和誰結合？結合前後半衰期？ | 原文缺答案；需回查。醫學上 direct bilirubin 是 bilirubin glucuronide，另 delta bilirubin 與 albumin 共價結合、半衰期接近 albumin。 | Q: 2003; A: 無 | raw 沒有半衰期答案，不可視為完整。 | `agent_D_segments_25_31.md` |
| S30-Q05 | 修正 | 哺乳性黃疸 breastfeeding jaundice：病因、時間、母乳餵多或少？ | Suboptimal intake jaundice：母乳攝取不足/脫水，腸肝循環增加；多在出生後 2-3天或第一週；處置是增加餵奶。 | Q: 2007-2013; A: 2053-2059 | 原文寫「又稱生理性黃疸」不精確；breastfeeding jaundice 是攝取不足型。 | `agent_D_segments_25_31.md` |
| S30-Q06 | 修正 | 母乳性黃疸 breast milk jaundice：病因、時間、母乳餵多或少？ | 母乳成分使 unconjugated bilirubin 增加，常見機轉含 beta-glucuronidase；多在第 1-2週出現、可持續數週；通常繼續母乳，嚴重時依 phototherapy threshold，少數才短暫停餵。 | Q: 2015-2017; A: 2061-2065 | 原文寫處置是禁止母奶；現行觀念多為繼續母乳，除非嚴重或需鑑別時短暫中斷。 | `agent_D_segments_25_31.md` |
| S30-Q08 | 修正 | 新生兒膽道閉鎖 gold standard、病理、幾天內做什麼手術？ | Gold standard：intraoperative cholangiography；肝切片可見 bile duct proliferation/portal fibrosis/bile plugs；60天內做 Kasai portoenterostomy。 | Q: 2021-2023; A: 2067-2069 | 原文把肝臟切片寫成黃金標準；切片是重要檢查，確診黃金標準通常是術中膽道攝影。 | `agent_D_segments_25_31.md` |
| S31-Q03 | 疑義 | 慢性活動肝炎對應 HLA？ | 較常考 autoimmune hepatitis/chronic active hepatitis：HLA-B8、DR3/DR4；原文 B12 需回查。 | Q: 2081; A: 2119 | 原文寫 HLA-B8/B12；B12 不是常見現代考點。 | `agent_D_segments_25_31.md` |
| S31-Q12 | 修正 | Valproic acid 小心 SJS 對應 HLA？ | 沒有典型必背 HLA-SJS 對應；相較 aromatic AED，valproate 不是這組主考藥。 | Q: 2105; A: 2141 | 原文藥名拼成 Vaporic acid，應為 valproic acid。 | `agent_D_segments_25_31.md` |
| S31-Q15 | 修正 | Abacavir 對應 HLA？ | HLA-B*57:01；重點是 abacavir hypersensitivity，不是典型 SJS 主軸。 | Q: 2111; A: 2147 | 原文放在「藥物小心 SJS」下，容易誤以為 abacavir 主考 SJS。 | `agent_D_segments_25_31.md` |
| S32-Q01 | 缺答案 | Child-Pugh score 怎麼算？怎麼分 stage？ | 缺原文答案。 | Q: 2153; A: 無 | 原 segment 只有題目清單。 | `agent_E_segments_32_40.md` |
| S32-Q02 | 缺答案 | CHA2DS2-VASc score 怎麼算？幾分以上要處置？ | 缺原文答案。 | Q: 2155; A: 無 | 原文寫 CHADS2-VaSc，應為 CHA2DS2-VASc。 | `agent_E_segments_32_40.md` |
| S32-Q03 | 缺答案 | 代謝症候群怎麼診斷？ | 缺原文答案。 | Q: 2157; A: 無 | 原 segment 只有題目清單。 | `agent_E_segments_32_40.md` |
| S32-Q04 | 缺答案 | BISAP 怎麼算？用於什麼時間？ | 缺原文答案。 | Q: 2159; A: 無 | 原 segment 只有題目清單。 | `agent_E_segments_32_40.md` |
| S32-Q05 | 缺答案 | ABCD2 score 怎麼算？分數對應再中風風險？ | 缺原文答案。 | Q: 2161; A: 無 | 原 segment 只有題目清單。 | `agent_E_segments_32_40.md` |
| S32-Q06 | 缺答案 | TIMI score 怎麼算？幾分以上使用哪種治療有好處？ | 缺原文答案。 | Q: 2163; A: 無 | 原 segment 只有題目清單。 | `agent_E_segments_32_40.md` |
| S32-Q07 | 缺答案 | qSOFA 怎麼算？ | 缺原文答案。 | Q: 2165; A: 無 | 原 segment 只有題目清單。 | `agent_E_segments_32_40.md` |
| S32-Q08 | 缺答案 | SOFA 有哪幾項？ | 缺原文答案。 | Q: 2167; A: 無 | 原 segment 只有題目清單。 | `agent_E_segments_32_40.md` |
| S32-Q09 | 缺答案 | Apgar 有哪幾項？怎麼算？ | 缺原文答案。 | Q: 2171; A: 無 | 原 segment 只有題目清單。 | `agent_E_segments_32_40.md` |
| S32-Q10 | 缺答案 | Bishop score 有哪幾項？怎麼算？ | 缺原文答案。 | Q: 2173; A: 無 | 原 segment 只有題目清單。 | `agent_E_segments_32_40.md` |
| S32-Q11 | 缺答案 | POP-Q stage 九宮格代表什麼？stage 怎麼算？ | 缺原文答案。 | Q: 2175; A: 無 | 原 segment 只有題目清單。 | `agent_E_segments_32_40.md` |
| S32-Q12 | 缺答案 | 胎兒 Biophysical profile（BPP）怎麼算？滿分幾分？何時需引產？ | 缺原文答案。 | Q: 2177-2179; A: 無 | 原 segment 只有題目清單。 | `agent_E_segments_32_40.md` |
| S32-Q13 | 缺答案 | Preeclampsia severe features 有哪些？ | 缺原文答案。 | Q: 2181; A: 無 | 原 segment 只有題目清單。 | `agent_E_segments_32_40.md` |
| S32-Q14 | 缺答案 | 妊娠糖尿病怎麼診斷？ | 缺原文答案。 | Q: 2183; A: 無 | 原 segment 只有題目清單。 | `agent_E_segments_32_40.md` |
| S33-Q03 | 缺答案 | 氣喘急性惡化時 PE 要看什麼？ | 缺原文答案。 | Q: 2191; A: 無 | 可回查呼吸功、輔助肌使用、silent chest、意識、發紺。 | `agent_E_segments_32_40.md` |
| S33-Q05 | 修正 | Bronchodilator 後 FEV1 要改善多少才像氣喘？未達時鑑別診斷？ | FEV1 增加大於 12% 且大於 200 mL 支持氣喘；若固定阻塞再考慮 COPD，DLCO 低偏 emphysema，正常或高偏 chronic bronchitis 或 asthma。 | Q: 2197-2199; A: 2239-2241 | 原文只寫大於 12%，且把未達標直接導向 COPD，過度簡化。 | `agent_E_segments_32_40.md` |
| S33-Q07 | 修正 | 哪些氣喘病人更建議用 inhaled corticosteroid（ICS，相較 LAMA）？ | Type 2 或 eosinophilic asthma：血 eosinophil 大於等於 300/uL、痰 eosinophil 大於 2-3%、FeNO 高、過敏表現者較吃 ICS。 | Q: 2205; A: 2249-2251 | 原文把大於 300 寫成痰中 eosinophil，較像血 eosinophil cutoff。 | `agent_E_segments_32_40.md` |
| S33-Q10 | 修正 | 非 Type 2 asthma 的發炎路徑？ | 空汙、病毒、抽菸等刺激 Th17 或 innate pathway，IL-6、IL-8、IL-17 上升，吸引 neutrophil。 | Q: 2221-2223; A: 2263-2265 | 原文寫結核菌，作為非 Type 2 asthma 刺激源過窄且易誤導。 | `agent_E_segments_32_40.md` |
| S34-Q04 | 缺答案 | CURB-65 怎麼背？ | 缺原文答案。 | Q: 2279; A: 2305 | 原文只寫回去翻第 45 題，未列 criteria。 | `agent_E_segments_32_40.md` |
| S34-Q06 | 修正 | 可 cover Pseudomonas aeruginosa（PsA）的抗生素？ | Piperacillin-tazobactam、cefoperazone、ceftazidime、cefepime、anti-pseudomonal carbapenem（imipenem、meropenem；不含 ertapenem）、ciprofloxacin 或 levofloxacin、colistin、amikacin、gentamicin。 | Q: 2285; A: 2309-2313 | 修正拼字與分類；moxifloxacin 不可靠 cover PsA。 | `agent_E_segments_32_40.md` |
| S34-Q07 | 修正 | 可 cover MRSA 的抗生素？ | Vancomycin、teicoplanin、linezolid、daptomycin（不可用於肺炎）、ceftaroline；輕症或特定情境可用 TMP-SMX、doxycycline、clindamycin。 | Q: 2287; A: 2315-2319 | 原文列 daptomycin 但本段是肺炎脈絡，需註明不能治 MRSA pneumonia。 | `agent_E_segments_32_40.md` |
| S34-Q09 | 疑義 | 台灣社區型肺炎常見病原前五名？ | 原文口訣：Streptococcus pneumoniae 大於 Mycoplasma pneumoniae 大於 Chlamydia pneumoniae 大於 Klebsiella pneumoniae 大於 Haemophilus influenzae。 | Q: 2291; A: 2323 | 排名受年齡、住院族群與資料來源影響，需依題源確認。 | `agent_E_segments_32_40.md` |
| S35-Q02 | 修正 | 辨識小細胞肺癌的神經內分泌 marker？ | Chromogranin、synaptophysin、CD56/NCAM、INSM1；傳統也可見 NSE。 | Q: 2331; A: 2377 | 原文把 CD56 與 NCAM 分開列成兩項，但 CD56 即 NCAM。 | `agent_E_segments_32_40.md` |
| S35-Q07 | 修正 | 肺鱗癌與肺腺癌的 Napsin A、TTF-1、CK7、CK20 表現？ | 肺腺癌：Napsin A+、TTF-1+、CK7+、CK20-；肺鱗癌：p40/p63+、Napsin A-、TTF-1-，CK7 可變，CK20 通常陰性。 | Q: 2343-2345; A: 2387-2399 | 原文把鱗癌簡化成 CK7-/CK20-，CK7 並非可靠雙陰記法。 | `agent_E_segments_32_40.md` |
| S35-Q08 | 修正 | 肺腺癌、肺鱗癌、小細胞癌的周邊性、腦轉移、預後與 paraneoplastic syndrome？ | 周邊：肺腺癌常見；腦轉移：small cell 高，NSCLC 中 adenocarcinoma 高於 squamous；預後概念：small cell 最差，NSCLC 視 stage 與 mutation。高血鈣/PTHrP：squamous；Lambert-Eaton、SIADH、Cushing：small cell；Horner：Pancoast tumor 壓迫交感神經，不是單純細胞型；hypertrophic osteoarthropathy：常見於 adenocarcinoma/NSCLC。 | Q: 2347-2359; A: 2401-2407 | 原文腦轉移排序寫 SCC 大於 adenocarcinoma，且把 Horner 直接歸 SCC，皆易誤導。 | `agent_E_segments_32_40.md` |
| S35-Q09 | 修正 | Trousseau syndrome 是什麼？ | 惡性腫瘤造成的遊走性血栓靜脈炎/高凝血狀態；典型見於胰臟、胃、肺腺癌等 adenocarcinoma。 | Q: 2361; A: 2409-2411 | 原文只說是肺癌 paraneoplastic syndrome，太限縮。 | `agent_E_segments_32_40.md` |
| S35-Q10 | 疑義 | Stage 多少以上 NSCLC 需 routine 腦部 MRI？ | 常考舊口徑可記 stage III 以上；部分新版 guideline 對 stage II 以上或治癒意圖治療前也建議 brain MRI。Small cell lung cancer 不論 stage 都要評估腦轉移。 | Q: 2363; A: 2413 | NSCLC 腦 MRI 門檻依 guideline 與年代不同。 | `agent_E_segments_32_40.md` |
| S36-Q02 | 修正 | PE、myxedema、uremia、Meigs、LAM 胸水分類與相關疾病？ | Pulmonary embolism 多為 exudate；myxedema 可 transudate 或 exudate；uremia 為 exudate；Meigs syndrome 多為 exudative pleural effusion；lymphangioleiomyomatosis（LAM）與 tuberous sclerosis complex 相關，常見 chylous exudate。 | Q: 2425-2429; A: 2455-2459 | 原文未回答 LAM 與 tuberous sclerosis complex 相關；myxedema 單列 transudate 過度簡化。 | `agent_E_segments_32_40.md` |
| S36-Q06 | 修正 | 懷疑肉芽腫/TB 胸水驗什麼？TB 大於多少？小於多少可排除？ | 驗 pleural fluid adenosine deaminase（ADA）；大於 40 U/L 支持 TB，超過 70 更強；小於 40 較可排除 TB pleuritis。 | Q: 2439-2441; A: 2473 | 原文只用大於 70 作懷疑門檻，對常考 ADA 大於 40 口徑偏嚴。 | `agent_E_segments_32_40.md` |
| S37-Q08 | 修正 | 腎上腺疾病的色素沉著為何？哪些疾病會見到？ | ACTH 上升刺激 melanocortin receptor；見於 primary adrenal insufficiency，也可見於 ACTH-dependent Cushing（pituitary 或 ectopic ACTH），不見於 adrenal tumor 或外源性 steroid 造成的 ACTH 低下。 | Q: 2499-2503; A: 2541 | 原文寫 Cushing syndrome 與腎上腺低下都會出現，未限定 ACTH 高的型態。 | `agent_E_segments_32_40.md` |
| S38-Q03 | 修正 | VHL、NF1、NF2 表現？ | VHL：clear cell renal cell carcinoma、retinal/cerebellar hemangioblastoma、pheochromocytoma、pancreatic/renal cyst、polycythemia。NF1：cafe-au-lait spots、Lisch nodules、neurofibromas、optic glioma、learning disability/骨病變、pheo。NF2：bilateral vestibular schwannoma、meningioma、ependymoma。 | Q: 2555-2557; A: 2601-2609 | 原文把 NF2 寫成視網膜 hamartoma，較不典型；NF2 高頻是 ependymoma/meningioma/vestibular schwannoma。 | `agent_E_segments_32_40.md` |
| S38-Q09 | 修正 | 哪種貧血與骨科/骨病也會有 cafe-au-lait spot？ | Fanconi anemia；McCune-Albright syndrome（fibrous dysplasia 相關）。 | Q: 2575-2577; A: 2625 | 原文 Fanconi 拼字誤作 Faconi。 | `agent_E_segments_32_40.md` |
| S39-Q08 | 修正 | 產後 milk ejection 由什麼激素引起？被誰抑制？ | Milk ejection/let-down 由 oxytocin 引起；壓力、疼痛、catecholamine 可抑制 let-down。Dopamine 抑制的是 prolactin 分泌與 milk production。 | Q: 2653; A: 2693 | 原文把 dopamine 寫成抑制 milk ejection，易與 prolactin 抑制混淆。 | `agent_E_segments_32_40.md` |
| S40-Q10 | 修正 | 先天甲狀腺低下與 10 歲小孩甲狀腺低下最常見原因？ | 先天最常見 thyroid dysgenesis/ectopy；學齡兒童常見 Hashimoto thyroiditis。 | Q: 2757-2761; A: 2759 | 原文「甲狀腺異味」應為「甲狀腺異位」。 | `agent_E_segments_32_40.md` |
| S40-Q12 | 疑義 | Plummer 指什麼？什麼情況會出現？ | Plummer nails 指 onycholysis（指甲與甲床分離），可見於 hyperthyroidism/Graves；但 Plummer disease 另指 toxic multinodular goiter。 | Q: 2769; A: 2771 | 原題只寫 Plummer，需分清 Plummer nails 與 Plummer disease。 | `agent_E_segments_32_40.md` |
| S40-Q14 | 修正 | 甲狀腺風暴怎麼治？ | 支持治療與處理誘因；beta-blocker；thionamide（PTU 優先，也可 methimazole）；至少 1 小時後給 iodine/Lugol 抑制釋放；給 glucocorticoid 抑制 T4 轉 T3 並防 adrenal insufficiency。 | Q: 2781; A: 2783-2785 | 原文漏 glucocorticoid，且「以防 Wolff-Chaikoff」說法錯；Wolff-Chaikoff 是 iodine 抑制合成的效果。 | `agent_E_segments_32_40.md` |
| S40-Q15 | 修正 | 疼痛型甲狀腺炎怎麼治？ | Subacute painful thyroiditis：NSAID 或 aspirin；嚴重疼痛或反應差可給 steroid；甲亢症狀用 beta-blocker。 | Q: 2787; A: 2789, 2793 | 原答案行序交錯，單寫 steroid 不完整。 | `agent_E_segments_32_40.md` |
| S40-Q17 | 修正 | PTU 系列藥物最常見與最嚴重副作用？ | Thionamide 常見副作用是 rash/pruritus；嚴重副作用為 agranulocytosis，PTU 還要記 severe hepatotoxicity。 | Q: 2795; A: 2801 | 原文只列 agranulocytosis，PTU 的嚴重肝毒性也高頻。 | `agent_E_segments_32_40.md` |
| S41-Q01 | 修正 | 甲狀腺癌如果有症狀，通常是甲亢還是甲低下？ | 多數甲狀腺癌 thyroid function 正常；若問結節風險，cold/nonfunctioning nodule 比 hot nodule 可疑，非典型甲亢。 | Q: 2807; A: 2849 | 原文寫「通常是甲低下」太絕對，易誤導成癌症常造成 hypothyroidism。 | `agent_F_segments_41_49.md` |
| S41-Q03 | 修正 | 甲狀腺結節哪些年齡、性別、觸診、病史、症狀、PE 會更懷疑癌？ | 年齡 <20 或 >60-70、男性、硬且固定、頸部放射線史、聲音沙啞或 dysphonia（發聲困難）、頸部淋巴結腫大。 | Q: 2811-2815; A: 2853-2855 | 原文用 >70，可保留但建議記成高齡危險，部分教材用 >60。 | `agent_F_segments_41_49.md` |
| S41-Q04 | 修正 | 甲狀腺癌的超音波 finding 講五個。 | 低回音、實心、邊緣不規則或浸潤、微鈣化、高度 > 寬度。 | Q: 2817; A: 2857-2861 | 原文另列 >20 mm，較像 FNA 門檻或風險加權，不是典型五大惡性超音波特徵之一。 | `agent_F_segments_41_49.md` |
| S41-Q06 | 修正 | Papillary ca 哪個性別預後好？Follicular ca 呢？ | 分化型甲狀腺癌整體女性預後較好，男性較差；Papillary、Follicular 都可用此方向。 | Q: 2823; A: 2865 | 原文只寫「女性預後好」，未明示 follicular 也同方向。 | `agent_F_segments_41_49.md` |
| S41-Q07 | 缺答案 | 通常年紀如何預後會比較好？ | 原文缺答案；校對：年輕預後較好，AJCC 第 8 版分化型甲狀腺癌以 <55 歲作重要分期切點。 | Q: 2825; A: - | 答案群未配到此題。 | `agent_F_segments_41_49.md` |
| S42-Q01 | 修正 | 糖尿病怎麼診斷？糖尿病前期是什麼？ | DM：FPG ≥126 mg/dL、HbA1c ≥6.5%、75 g OGTT 2 hr ≥200 mg/dL、或典型症狀 + random glucose ≥200 mg/dL。PreDM：HbA1c 5.7-6.4%、FPG 100-125、OGTT 2 hr 140-199。 | Q: 2893; A: 2931-2935 | 原文用 `>`，診斷門檻應用 `≥`。 | `agent_F_segments_41_49.md` |
| S42-Q02 | 缺答案 | 妊娠糖尿病怎麼診斷？通常懷孕幾週發生/篩檢？ | 原文缺 GDM 診斷 criteria；篩檢通常在 24-28 週。 | Q: 2895-2897; A: 2937-2939 | 答案寫「criteria 補充在下頁」，本 segment 未收錄；不可假裝完整。 | `agent_F_segments_41_49.md` |
| S42-Q09 | 修正 | 糖尿病視網膜病變：BDR 三個、PPDR 兩個、PDR 一個。 | BDR/NPDR：microaneurysm（微血管瘤）、retinal hemorrhage（視網膜出血）、hard exudate（硬性滲出）/macular edema。PPDR：cotton-wool spots、IRMA（intraretinal microvascular abnormalities，視網膜內微血管異常）/venous beading。PDR：neovascularization（新生血管），可併 vitreous hemorrhage。 | Q: 2915-2917; A: 2965-2969 | 原文 PDR 只寫 vitreous hemorrhage；真正分類核心是 neovascularization。 | `agent_F_segments_41_49.md` |
| S42-Q11 | 修正 | 糖尿病用藥副作用：體重減輕/增加、類天皰瘡、胰臟炎、低血糖、心衰竭、水腫、肝指數上升？ | 體重減輕：SGLT2 inhibitor、GLP-1 receptor agonist。體重增加：SU、TZD、insulin。類天皰瘡：DPP-4 inhibitor。胰臟炎：DPP-4 inhibitor、GLP-1 receptor agonist。低血糖：SU、insulin。HF：TZD、saxagliptin。水腫：TZD。肝指數上升：acarbose 可見。 | Q: 2923-2927; A: 2977-2983 | 原文少列 GLP-1 RA 的胰臟炎風險；其餘方向可用。 | `agent_F_segments_41_49.md` |
| S43-Q01 | 修正 | DKA 怎麼診斷？ | Hyperglycemia（常 >250 mg/dL）、ketonemia/ketonuria、metabolic acidosis（pH <7.3 或 HCO3 ≤18）且 anion gap 增加。 | Q: 2989; A: 3021-3023 | 原文未寫 pH，HCO3 寫 15-18 可保留但建議用 ≤18 作考試骨架。 | `agent_F_segments_41_49.md` |
| S43-Q04 | 修正 | DKA 第一線治療？ | 先輸液復水；接著依 K 值補鉀並給 IV insulin（K <3.3 時先補鉀再 insulin）。 | Q: 2995; A: 3033 | 原文「視情況給 insulin」太弱，DKA 治療核心是 fluid、insulin、potassium。 | `agent_F_segments_41_49.md` |
| S43-Q11 | 修正 | HHS 怎麼治療？ | 第一線大量輸液；之後依 K 值、滲透壓與血糖下降速度給 insulin 與電解質校正。 | Q: 3013; A: 3055 | 原文只寫輸液，需補 insulin/K 監測才完整。 | `agent_F_segments_41_49.md` |
| S44-Q01 | 疑義 | 腦膜炎傳統 triad？ | 常考可見：發燒、頭痛、頸部僵硬；若題目寫 classic bacterial meningitis triad，也常指發燒、頸僵、意識改變。 | Q: 3063; A: 3091 | 原文只列發燒/頭痛/頸僵；不同教材的「classic triad」會把 headache 換成 altered mental status。 | `agent_F_segments_41_49.md` |
| S44-Q02 | 修正 | Kernig sign 跟 Brudzinski sign 怎麼做？ | Kernig：仰臥，髖膝屈曲後被動伸膝，引發疼痛/阻力。Brudzinski：被動屈頸時髖膝反射性屈曲。 | Q: 3065; A: 3093-3095 | 原文只有記憶法，沒有真正操作方式。 | `agent_F_segments_41_49.md` |
| S45-Q05 | 修正 | 牙科手術後 IE、靜脈毒癮 IE、人工瓣膜 IE 各猜哪隻菌？ | 牙科：viridans streptococci。IVDU：Staphylococcus aureus。人工瓣膜：早期常見 coagulase-negative staphylococci（如 S. epidermidis）與 S. aureus；晚期較像 native valve。 | Q: 3139-3141; A: 3185 | 原文人工瓣膜只寫 S. aureus，少了考試常見的 S. epidermidis/CoNS。 | `agent_F_segments_41_49.md` |
| S46-Q02 | 修正 | Vibrio cellulitis 用什麼抗生素？ | Doxycycline（或 tetracycline 類）+ third-generation cephalosporin（常考 ceftazidime）。 | Q: 3217; A: 3243 | 原文寫「3 代 cepha + tetracycline」方向可用；整理成常用藥名。 | `agent_F_segments_41_49.md` |
| S47-Q04 | 修正 | 懷孕婦女不能用的抗生素四類？ | 常考避免：tetracycline/tigecycline、aminoglycosides、fluoroquinolones、sulfonamides（trimester/近足月需分情境）。 | Q: 3293; A: 3317-3319 | 原文列 tetracycline、AG、tigecycline、sulfonamide，但少了常考 FQ；sulfonamide 不是全孕期絕對禁忌。 | `agent_F_segments_41_49.md` |
| S47-Q05 | 修正 | 哪一類抗生素副作用有 QT prolongation？ | Fluoroquinolones 可 QT prolongation；macrolides 也常考 QT prolongation。 | Q: 3295; A: 3321 | 原文只寫 FQ，若選項有 macrolide 也要小心。 | `agent_F_segments_41_49.md` |
| S47-Q06 | 疑義 | 哪個抗結核藥會跟 NRTIs 有交互作用，TB + HIV 要慎用？ | Rifampin；但重點應是 rifampin 會與多種 antiretroviral therapy（ART）交互作用，尤其 PI/NNRTI/部分 integrase inhibitor，不是典型只針對 NRTI。 | Q: 3297-3299; A: 3323 | 原題或原文把 NRTI 寫成主要交互作用對象可能不精確；需回查題源。 | `agent_F_segments_41_49.md` |
| S48-Q07 | 疑義 | Mycotic aneurysm 最常見病原菌？ | 常見是 Staphylococcus aureus、Salmonella spp.；endocarditis 相關也可見 Streptococcus。 | Q: 3343; A: 3387-3389 | 原文列 Staph/Strep/Salmonella 並說不是 fungus；若題目問「最常見」單選，需看題源情境。 | `agent_F_segments_41_49.md` |
| S48-Q08 | 疑義 | Open 和 EVAR，哪個使用 CSF drainage 會沒有保護效果？ | 疑義：CSF drainage 主要用於 open thoracoabdominal aortic repair 或高風險 endovascular thoracic repair 的 spinal cord protection；一般 AAA EVAR 非例行。 | Q: 3345; A: 3391 | 原題問「哪個沒有保護效果」，原文答「都有保護效果」互相衝突；需回查題源。 | `agent_F_segments_41_49.md` |
| S48-Q10 | 缺答案 | 影響 AAA 手術結果最重要危險因素？ | 原文缺答案；需回查來源。 | Q: 3349; A: 3395 | 答案只寫 indication 在下頁，未回答此題。 | `agent_F_segments_41_49.md` |
| S48-Q11 | 缺答案 | TAA 開刀 indication？ | 原文缺答案；需回查來源。 | Q: 3351; A: 3395 | 答案寫在下一頁，本 segment 未收錄；不可假裝完整。 | `agent_F_segments_41_49.md` |
| S48-Q12 | 缺答案 | AAA 開刀 indication？ | 原文缺答案；需回查來源。 | Q: 3353; A: 3395 | 答案寫在下一頁，本 segment 未收錄；不可假裝完整。 | `agent_F_segments_41_49.md` |
| S48-Q13 | 缺答案 | Crawford classification type I-V 分別為何？ | 原文缺答案；需回查來源。 | Q: 3355; A: 3397 | 答案寫補充在下頁/下下頁，本 segment 未收錄。 | `agent_F_segments_41_49.md` |
| S48-Q14 | 缺答案 | AAA 做完 EVAR 後 Endoleak type I-V 分別發生在哪裡？ | 原文缺答案；需回查來源。 | Q: 3357-3359; A: 3397 | 答案寫補充在下頁/下下頁，本 segment 未收錄。 | `agent_F_segments_41_49.md` |
| S48-Q15 | 缺答案 | AoD 的 DeBakey 與 Stanford 分類？ | 原文缺答案；需回查來源。 | Q: 3361-3363; A: 3397 | 答案寫補充在下頁/下下頁，本 segment 未收錄。 | `agent_F_segments_41_49.md` |
| S48-Q16 | 修正 | IABP 放在哪段主動脈？何時充氣/消氣？禁忌？對 MI 後 cardiogenic shock 死亡率有好處嗎？ | IABP balloon 位於 descending thoracic aorta（tip 在 left subclavian distal、renal arteries proximal）。Diastole 充氣、systole 前快速消氣。禁忌：aortic regurgitation、aortic dissection、severe PAD。MI 後 cardiogenic shock 不建議常規使用，無明確死亡率改善。 | Q: 3365-3369; A: 3399-3405 | 原文「舒張中期消氣」不對，應在收縮前/舒張末消氣以降低 afterload。 | `agent_F_segments_41_49.md` |
| S49-Q04 | 修正 | 腹痛 + 無痛性血便猜什麼？影像診斷？第二常見表現？Rule of 2？異位組織？ | Meckel diverticulum（梅克爾憩室）。診斷：Tc-99m pertechnetate scan。第二常見表現原文缺；常考可記 obstruction/intussusception。Rule of 2：2% 人口、距 ileocecal valve 2 feet、長 2 inches、2 歲前常出現症狀、2:1 男性、2 種異位組織。異位組織：胃黏膜最常見，其次胰臟。 | Q: 3421-3425; A: 3459-3467 | 原文寫 Meckel's diverticulitis 不精確，無痛性血便應是 Meckel diverticulum；答案也漏「第二常見表現」。 | `agent_F_segments_41_49.md` |
| S49-Q05 | 修正 | 噴射非膽汁嘔吐 + olive mass 猜什麼？族群、性別、發病時點、X 光、鋇劑、超音波、治療、術式名？ | Hypertrophic pyloric stenosis（肥厚性幽門狹窄）。白種人、男嬰多，2-8 週。X-ray：single bubble/胃擴張。UGI：string sign、shoulder sign、double-track sign。US：肌層厚 >3 mm、直徑 >13-14 mm、長度 >15-17 mm。Tx：pyloromyotomy，又稱 Ramstedt procedure。 | Q: 3427-3431; A: 3469-3479 | 原文 Ramstedt 拼字錯；影像 cutoff 依教材略有差異。 | `agent_F_segments_41_49.md` |
| S49-Q06 | 疑義 | 胰臟炎、腸阻塞、闌尾炎、腸套疊、小腸阻塞、子宮外孕中，哪些痛感會轉移到背？ | 最典型是 pancreatitis（胰臟炎）背痛/放射到背；retrocecal appendicitis 可背/腰痛但非典型；腸阻塞不是典型「轉移到背」。 | Q: 3433-3435; A: 3481 | 原文列胰臟炎、腸阻塞、闌尾炎；若考題單選或典型表現，腸阻塞/闌尾炎需回查題源。 | `agent_F_segments_41_49.md` |
