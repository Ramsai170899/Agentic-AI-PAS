import React, { useState, useMemo } from 'react';
import { 
  LayoutDashboard, 
  FileText, 
  Users, 
  Bell, 
  ShieldCheck, 
  BrainCircuit, 
  Activity, 
  ChevronRight, 
  Search, 
  AlertTriangle, 
  CheckCircle2, 
  History, 
  FileSearch,
  Zap,
  MoreVertical,
  Scale,
  MessageSquareQuote,
  ArrowUpRight
} from 'lucide-react';

// --- Mock Data ---
const MOCK_CASES = [
  { id: 'L-8829', name: 'Alexander Thompson', faceAmount: '$2,500,000', status: 'Pending Review', risk: 'High', signals: ['Income Mismatch', 'Adverse Lab'], age: 45, type: 'Whole Life' },
  { id: 'L-9012', name: 'Elena Rodriguez', faceAmount: '$500,000', status: 'New', risk: 'Low', signals: ['Clean History'], age: 32, type: 'Term 20' },
  { id: 'L-8744', name: 'Marcus Chen', faceAmount: '$1,200,000', status: 'In Progress', risk: 'Medium', signals: ['Tobacco Use Discrepancy'], age: 51, type: 'Universal Life' },
];

const CASE_DETAILS = {
  id: 'L-8829',
  applicant: 'Alexander Thompson',
  age: 45,
  faceAmount: '$2,500,000',
  medical: [
    { label: 'BMI', value: '31.2', status: 'warning', ai_note: 'Class 1 Obesity detected' },
    { label: 'Blood Pressure', value: '142/92', status: 'danger', ai_note: 'Consistent with Stage 2 Hypertension' },
    { label: 'A1C', value: '5.8%', status: 'warning', ai_note: 'Pre-diabetic threshold' }
  ],
  financial: [
    { label: 'Annual Income', declared: '$150,000', verified: '$110,000', status: 'danger', ai_note: '27% variance from tax transcripts' },
    { label: 'Total Assets', value: '$1.2M', status: 'normal' }
  ],
  ai_rationale: [
    { step: 'Data Aggregation', detail: 'Ingested 42 pages of APS and Lab records.', confidence: 99 },
    { step: 'Pattern Recognition', detail: 'Cross-referenced MIB records showing undisclosed specialist visit (Cardiology, 2023).', confidence: 94 },
    { step: 'Guideline Alignment', detail: 'Matches Table D criteria based on comorbid Hypertension and BMI.', confidence: 88 }
  ]
};

// --- Components ---

const SidebarItem = ({ icon: Icon, label, active, onClick }) => (
  <button 
    onClick={onClick}
    className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
      active ? 'bg-teal-900/30 text-teal-400 border-l-2 border-teal-500' : 'text-slate-400 hover:bg-slate-800'
    }`}
  >
    <Icon size={18} />
    <span className="text-sm font-medium">{label}</span>
  </button>
);

const RiskBadge = ({ level }) => {
  const colors = {
    High: 'bg-red-950 text-red-400 border-red-800',
    Medium: 'bg-amber-950 text-amber-400 border-amber-800',
    Low: 'bg-emerald-950 text-emerald-400 border-emerald-800'
  };
  return (
    <span className={`px-2 py-0.5 rounded text-[10px] font-bold border uppercase tracking-wider ${colors[level]}`}>
      {level} Risk
    </span>
  );
};

export default function App() {
  const [activeTab, setActiveTab] = useState('dashboard'); // 'dashboard' or 'case'
  const [selectedCase, setSelectedCase] = useState(null);
  const [decisionMode, setDecisionMode] = useState('standard');

  const handleOpenCase = (caseId) => {
    setSelectedCase(CASE_DETAILS);
    setActiveTab('case');
  };

  return (
    <div className="flex h-screen bg-[#0a0f18] text-slate-200 font-sans selection:bg-teal-500/30">
      
      {/* 1. ORCHESTRATION LAYER (Nav) */}
      <aside className="w-64 border-r border-slate-800 flex flex-col bg-[#0d131f]">
        <div className="p-6 flex items-center gap-2">
          <div className="w-8 h-8 bg-teal-600 rounded flex items-center justify-center">
            <ShieldCheck className="text-white" size={20} />
          </div>
          <span className="font-bold text-lg tracking-tight text-white">Aegis<span className="text-teal-500">PAS</span></span>
        </div>

        <nav className="flex-1 px-3 space-y-1">
          <div className="text-[10px] uppercase font-bold text-slate-500 px-4 mb-2 tracking-widest">Main</div>
          <SidebarItem icon={LayoutDashboard} label="Worklist Console" active={activeTab === 'dashboard'} onClick={() => setActiveTab('dashboard')} />
          <SidebarItem icon={FileText} label="Policy Lifecycle" />
          <SidebarItem icon={Users} label="Agent Portal" />
          <div className="pt-6 text-[10px] uppercase font-bold text-slate-500 px-4 mb-2 tracking-widest">Intelligence</div>
          <SidebarItem icon={Activity} label="Risk Analytics" />
          <SidebarItem icon={BrainCircuit} label="Model Performance" />
          <SidebarItem icon={History} label="Audit Logs" />
        </nav>

        <div className="p-4 border-t border-slate-800">
          <div className="flex items-center gap-3 p-2 bg-slate-800/50 rounded-lg">
            <div className="w-8 h-8 rounded-full bg-slate-600 border border-slate-500 flex items-center justify-center text-xs font-bold">JW</div>
            <div className="flex-1 min-w-0">
              <p className="text-xs font-semibold text-white truncate">Jonathan Weaver</p>
              <p className="text-[10px] text-slate-400">Senior Underwriter</p>
            </div>
          </div>
        </div>
      </aside>

      {/* MAIN CONTENT AREA */}
      <main className="flex-1 flex flex-col overflow-hidden">
        {/* Top Header */}
        <header className="h-14 border-b border-slate-800 flex items-center justify-between px-6 bg-[#0a0f18]">
          <div className="flex items-center gap-4 flex-1">
            <div className="relative w-96">
              <Search size={16} className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500" />
              <input 
                type="text" 
                placeholder="Search policy, applicant, or SSN..." 
                className="w-full bg-slate-900 border border-slate-700 rounded-md py-1.5 pl-10 pr-4 text-sm focus:outline-none focus:border-teal-500 transition-colors"
              />
            </div>
          </div>
          <div className="flex items-center gap-4">
            <div className="flex items-center gap-2 px-3 py-1 bg-teal-950/40 border border-teal-800 rounded-full text-teal-400">
              <Zap size={14} fill="currentColor" />
              <span className="text-xs font-bold italic tracking-wide">AI CO-PILOT ACTIVE</span>
            </div>
            <button className="relative text-slate-400 hover:text-white">
              <Bell size={20} />
              <span className="absolute -top-1 -right-1 w-2 h-2 bg-teal-500 rounded-full"></span>
            </button>
          </div>
        </header>

        {activeTab === 'dashboard' ? (
          /* DASHBOARD VIEW */
          <div className="flex-1 overflow-y-auto p-8 space-y-8">
            <div className="flex justify-between items-end">
              <div>
                <h1 className="text-2xl font-bold text-white">Underwriting Console</h1>
                <p className="text-slate-400 text-sm">System-prioritized case queue based on urgency and risk complexity.</p>
              </div>
              <div className="flex gap-2">
                <button className="px-4 py-2 bg-slate-800 border border-slate-700 rounded text-xs font-semibold hover:bg-slate-700 transition-colors">Export Report</button>
                <button className="px-4 py-2 bg-teal-600 text-white rounded text-xs font-semibold hover:bg-teal-500 transition-colors shadow-lg shadow-teal-900/20">Fetch New Cases</button>
              </div>
            </div>

            {/* Metrics Row */}
            <div className="grid grid-cols-4 gap-4">
              {[
                { label: 'Active Queue', val: '24', change: '+2', icon: FileText },
                { label: 'Pending Evidence', val: '12', change: '-4', icon: FileSearch },
                { label: 'Decision SLA %', val: '98.2', change: '+0.1', icon: Activity },
                { label: 'AI Confidence Avg', val: '84%', change: '+3%', icon: BrainCircuit }
              ].map((m, i) => (
                <div key={i} className="bg-slate-900/50 border border-slate-800 p-4 rounded-xl">
                  <div className="flex justify-between items-start mb-2">
                    <m.icon size={18} className="text-slate-500" />
                    <span className={`text-[10px] font-bold ${m.change.startsWith('+') ? 'text-emerald-500' : 'text-rose-500'}`}>{m.change}</span>
                  </div>
                  <div className="text-2xl font-bold text-white">{m.val}</div>
                  <div className="text-[10px] uppercase tracking-wider font-bold text-slate-500">{m.label}</div>
                </div>
              ))}
            </div>

            {/* Table */}
            <div className="bg-slate-900/30 border border-slate-800 rounded-xl overflow-hidden">
              <div className="px-6 py-4 border-b border-slate-800 flex justify-between items-center">
                <h3 className="text-sm font-bold text-white">Priority Worklist</h3>
                <div className="flex gap-4 text-xs">
                  <span className="text-slate-400">Filter: <span className="text-white font-medium">High Risk</span></span>
                  <span className="text-slate-400">Sort: <span className="text-white font-medium">Urgency</span></span>
                </div>
              </div>
              <table className="w-full text-left">
                <thead className="bg-slate-800/40 text-[10px] uppercase font-bold text-slate-500 tracking-widest">
                  <tr>
                    <th className="px-6 py-3">Applicant</th>
                    <th className="px-6 py-3">Case ID</th>
                    <th className="px-6 py-3">Face Amount</th>
                    <th className="px-6 py-3">Risk Level</th>
                    <th className="px-6 py-3">AI Signals</th>
                    <th className="px-6 py-3 text-right">Action</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800">
                  {MOCK_CASES.map((c) => (
                    <tr key={c.id} className="hover:bg-teal-500/5 transition-colors group">
                      <td className="px-6 py-4">
                        <div className="font-semibold text-white">{c.name}</div>
                        <div className="text-xs text-slate-500">{c.type} • Age {c.age}</div>
                      </td>
                      <td className="px-6 py-4 text-xs font-mono text-slate-400">{c.id}</td>
                      <td className="px-6 py-4 text-sm font-medium text-slate-300">{c.faceAmount}</td>
                      <td className="px-6 py-4">
                        <RiskBadge level={c.risk} />
                      </td>
                      <td className="px-6 py-4">
                        <div className="flex flex-wrap gap-1">
                          {c.signals.map((s, idx) => (
                            <span key={idx} className="text-[10px] bg-slate-800 px-1.5 py-0.5 rounded text-slate-400 border border-slate-700">{s}</span>
                          ))}
                        </div>
                      </td>
                      <td className="px-6 py-4 text-right">
                        <button 
                          onClick={() => handleOpenCase(c.id)}
                          className="bg-slate-800 group-hover:bg-teal-600 text-slate-300 group-hover:text-white p-2 rounded transition-all"
                        >
                          <ChevronRight size={16} />
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        ) : (
          /* 2. CASE WORKSPACE (Cockpit) */
          <div className="flex-1 flex overflow-hidden">
            
            {/* Central Decision Workspace */}
            <div className="flex-1 overflow-y-auto bg-[#0a0f18] border-r border-slate-800">
              <div className="p-8 space-y-8">
                {/* Header Context */}
                <div className="flex justify-between items-start">
                  <div className="flex items-center gap-4">
                    <button onClick={() => setActiveTab('dashboard')} className="text-slate-500 hover:text-white">
                      <History size={20} />
                    </button>
                    <div>
                      <div className="flex items-center gap-2">
                        <h1 className="text-2xl font-bold text-white">{selectedCase.applicant}</h1>
                        <span className="text-slate-500 font-mono text-sm tracking-tighter">CASE ID: {selectedCase.id}</span>
                      </div>
                      <div className="flex gap-4 mt-1 text-xs text-slate-400">
                        <span>Age: <strong className="text-slate-200">{selectedCase.age}</strong></span>
                        <span>Product: <strong className="text-slate-200">Executive Whole Life</strong></span>
                        <span>Face: <strong className="text-slate-200">{selectedCase.faceAmount}</strong></span>
                      </div>
                    </div>
                  </div>
                  <div className="flex gap-2">
                    <button className="flex items-center gap-2 px-3 py-1.5 bg-slate-800 border border-slate-700 rounded text-xs font-semibold hover:bg-slate-700">
                      <FileSearch size={14} /> View Evidence (12)
                    </button>
                  </div>
                </div>

                {/* Collapsible Data Sections */}
                <div className="space-y-4">
                  {/* Medical Data */}
                  <div className="border border-slate-800 rounded-xl overflow-hidden bg-slate-900/20">
                    <div className="px-4 py-3 bg-slate-800/40 border-b border-slate-800 flex justify-between items-center">
                      <div className="flex items-center gap-2 font-bold text-xs uppercase tracking-widest text-slate-300">
                        <Activity size={14} className="text-teal-400" /> Medical & Lab Metrics
                      </div>
                      <span className="text-[10px] text-teal-400 font-bold bg-teal-900/30 px-2 py-0.5 rounded uppercase">AI Verified</span>
                    </div>
                    <div className="p-4 grid grid-cols-3 gap-4">
                      {selectedCase.medical.map((item, i) => (
                        <div key={i} className={`p-3 border rounded-lg ${
                          item.status === 'danger' ? 'bg-red-950/20 border-red-900' : 'bg-slate-800/30 border-slate-700'
                        }`}>
                          <div className="text-xs text-slate-500 font-medium mb-1">{item.label}</div>
                          <div className="text-lg font-bold text-white flex items-center justify-between">
                            {item.value}
                            {item.status === 'danger' && <AlertTriangle size={14} className="text-red-500" />}
                          </div>
                          <div className="mt-2 flex items-start gap-1.5 bg-slate-900/50 p-1.5 rounded text-[10px] text-slate-400 leading-tight">
                            <BrainCircuit size={10} className="text-teal-500 shrink-0 mt-0.5" />
                            {item.ai_note}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Financial Discrepancies */}
                  <div className="border border-slate-800 rounded-xl overflow-hidden bg-slate-900/20">
                    <div className="px-4 py-3 bg-slate-800/40 border-b border-slate-800 flex justify-between items-center">
                      <div className="flex items-center gap-2 font-bold text-xs uppercase tracking-widest text-slate-300">
                        <Scale size={14} className="text-amber-500" /> Financial Justification
                      </div>
                      <span className="text-[10px] text-red-400 font-bold bg-red-900/30 px-2 py-0.5 rounded uppercase">Anomaly Detected</span>
                    </div>
                    <div className="p-4">
                      <div className="bg-red-950/10 border border-red-900/40 rounded-lg p-4 flex gap-4">
                        <div className="flex-1">
                          <h4 className="text-sm font-bold text-red-200 mb-2">Income Verification Conflict</h4>
                          <div className="grid grid-cols-2 gap-8">
                            <div>
                              <span className="text-[10px] uppercase font-bold text-slate-500 block">Applicant Declared</span>
                              <span className="text-xl font-bold text-slate-300">$150,000 /yr</span>
                            </div>
                            <div>
                              <span className="text-[10px] uppercase font-bold text-slate-500 block">AI Extracted (IRS-4506C)</span>
                              <span className="text-xl font-bold text-red-400">$110,000 /yr</span>
                            </div>
                          </div>
                          <p className="mt-3 text-xs text-slate-400 leading-relaxed italic">
                            Agentic AI reasoning: "The detected variance suggests a potential over-insurance risk. Tax transcript analysis confirms consistent income at lower tiers across the last 24 months."
                          </p>
                        </div>
                        <div className="flex flex-col gap-2">
                          <button className="px-3 py-1.5 bg-red-900 text-white text-[10px] font-bold rounded uppercase">Flag for Inquiry</button>
                          <button className="px-3 py-1.5 bg-slate-800 text-slate-300 text-[10px] font-bold rounded uppercase border border-slate-700">Accept Declared</button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                {/* Decisioning Panel */}
                <div className="border-t border-slate-800 pt-8 pb-12">
                  <h3 className="text-sm font-bold text-white mb-6 uppercase tracking-wider flex items-center gap-2">
                    <Zap size={16} className="text-teal-400" /> Final Risk Determination
                  </h3>
                  <div className="grid grid-cols-12 gap-6">
                    <div className="col-span-8 space-y-4">
                      <div className="grid grid-cols-2 gap-4">
                        <div className="p-4 bg-slate-900 border border-slate-700 rounded-lg">
                          <label className="text-[10px] font-bold text-slate-500 uppercase block mb-2 tracking-widest">Base Rating</label>
                          <select className="w-full bg-slate-800 border border-slate-600 rounded px-2 py-1.5 text-sm">
                            <option>Standard</option>
                            <option>Preferred</option>
                            <option selected>Table D (+100%)</option>
                            <option>Table F (+150%)</option>
                            <option>Decline</option>
                          </select>
                        </div>
                        <div className="p-4 bg-slate-900 border border-slate-700 rounded-lg">
                          <label className="text-[10px] font-bold text-slate-500 uppercase block mb-2 tracking-widest">Flat Extra</label>
                          <div className="flex gap-2">
                            <input type="text" placeholder="$0.00" className="flex-1 bg-slate-800 border border-slate-600 rounded px-2 py-1.5 text-sm" />
                            <span className="text-xs text-slate-500 mt-2">per $1k</span>
                          </div>
                        </div>
                      </div>
                      <div className="p-4 bg-teal-900/10 border border-teal-800/40 rounded-lg">
                        <div className="flex justify-between items-center mb-2">
                          <h4 className="text-xs font-bold text-teal-400 uppercase tracking-widest">AI Decision Simulation</h4>
                          <span className="text-[10px] text-teal-500 font-mono">CONFIDENCE: 88.4%</span>
                        </div>
                        <p className="text-xs text-slate-300 leading-relaxed mb-4">
                          Based on 14,000+ similar cases and 2024 Underwriting Guidelines, a Table D rating with Hypertension exclusions provides optimal risk mitigation while maintaining placement likelihood.
                        </p>
                        <div className="flex gap-4 border-t border-teal-800/30 pt-3">
                          <div className="flex-1">
                            <span className="text-[10px] text-slate-500 block uppercase font-bold">Projected Premium</span>
                            <span className="text-lg font-bold text-white">$4,120.00 <span className="text-[10px] text-slate-400">/annum</span></span>
                          </div>
                          <div className="flex-1">
                            <span className="text-[10px] text-slate-500 block uppercase font-bold">Placement Probability</span>
                            <span className="text-lg font-bold text-white">62%</span>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div className="col-span-4 flex flex-col gap-3">
                      <button className="w-full py-4 bg-teal-600 hover:bg-teal-500 text-white font-bold rounded-lg shadow-lg shadow-teal-900/40 transition-all flex items-center justify-center gap-2">
                        <CheckCircle2 size={18} /> Approve Policy
                      </button>
                      <button className="w-full py-3 bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold rounded-lg border border-slate-700 transition-all">
                        Request More Info
                      </button>
                      <button className="w-full py-3 bg-red-950/30 hover:bg-red-950/50 text-red-400 font-bold rounded-lg border border-red-900 transition-all">
                        Refer to Reinsurance
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* 3. AGENTIC AI CO-PILOT LAYER (Sidebar) */}
            <aside className="w-[380px] bg-[#0d131f] flex flex-col overflow-hidden">
              <div className="p-4 border-b border-slate-800 bg-[#111927]">
                <div className="flex items-center justify-between mb-4">
                  <div className="flex items-center gap-2">
                    <div className="w-6 h-6 rounded-full bg-teal-500 flex items-center justify-center animate-pulse">
                      <BrainCircuit size={14} className="text-white" />
                    </div>
                    <span className="font-bold text-xs uppercase tracking-tighter text-white">Underwriting Co-pilot</span>
                  </div>
                  <MoreVertical size={16} className="text-slate-500 cursor-pointer" />
                </div>
                <div className="bg-slate-900/80 border border-slate-700 p-3 rounded-lg">
                  <p className="text-[11px] text-slate-400 leading-snug">
                    <span className="text-teal-400 font-bold">Analysis Complete:</span> 3 critical risks and 2 favorable factors identified. Recommend Table D rating based on metabolic comorbid factors.
                  </p>
                </div>
              </div>

              <div className="flex-1 overflow-y-auto p-4 space-y-6">
                {/* Reasoning Chain */}
                <div>
                  <h4 className="text-[10px] uppercase font-black text-slate-500 tracking-widest mb-3 flex items-center gap-1.5">
                    <History size={12} /> Reasoning Chain
                  </h4>
                  <div className="space-y-4 border-l border-slate-800 ml-1.5 pl-4">
                    {selectedCase.ai_rationale.map((r, i) => (
                      <div key={i} className="relative">
                        <div className="absolute -left-[21px] top-1.5 w-2 h-2 rounded-full bg-slate-700 border border-slate-900 ring-4 ring-[#0d131f]"></div>
                        <div className="flex justify-between items-start">
                          <span className="text-xs font-bold text-slate-200">{r.step}</span>
                          <span className="text-[9px] font-bold text-teal-500 bg-teal-900/20 px-1 rounded">{r.confidence}% Match</span>
                        </div>
                        <p className="text-[11px] text-slate-500 mt-1 leading-relaxed">{r.detail}</p>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Proactive Drafts */}
                <div className="space-y-3">
                  <h4 className="text-[10px] uppercase font-black text-slate-500 tracking-widest mb-3 flex items-center gap-1.5">
                    <MessageSquareQuote size={12} /> Proactive Drafts
                  </h4>
                  <div className="p-3 bg-slate-800/40 border border-slate-700 rounded-lg group cursor-pointer hover:border-teal-500 transition-colors">
                    <div className="flex justify-between items-center mb-1">
                      <span className="text-[10px] font-bold text-white uppercase">Table D Rationale</span>
                      <ArrowUpRight size={12} className="text-slate-600 group-hover:text-teal-400" />
                    </div>
                    <p className="text-[10px] text-slate-500 italic line-clamp-2">"Based on BP of 142/92 and BMI of 31.2, applicant falls into..."</p>
                  </div>
                  <div className="p-3 bg-slate-800/40 border border-slate-700 rounded-lg group cursor-pointer hover:border-teal-500 transition-colors">
                    <div className="flex justify-between items-center mb-1">
                      <span className="text-[10px] font-bold text-white uppercase">Financial Inquiry</span>
                      <ArrowUpRight size={12} className="text-slate-600 group-hover:text-teal-400" />
                    </div>
                    <p className="text-[10px] text-slate-500 italic line-clamp-2">"Dear Agent, we require clarification on the income discrepancy..."</p>
                  </div>
                </div>

                {/* Comparable Cases */}
                <div>
                  <h4 className="text-[10px] uppercase font-black text-slate-500 tracking-widest mb-3 flex items-center gap-1.5">
                    <FileText size={12} /> Precedent Search
                  </h4>
                  <div className="space-y-2">
                    {[
                      { id: 'C-221', decision: 'Approve Std', match: '92%' },
                      { id: 'C-098', decision: 'Approve T-C', match: '87%' }
                    ].map((c, i) => (
                      <div key={i} className="flex items-center justify-between text-[11px] bg-slate-900/50 p-2 rounded">
                        <span className="text-slate-400 font-mono">{c.id}</span>
                        <span className="text-slate-300 font-bold">{c.decision}</span>
                        <span className="text-teal-600 font-bold">{c.match}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>

              {/* Chat Input area */}
              <div className="p-4 border-t border-slate-800 bg-[#0a0f18]">
                <div className="relative">
                  <textarea 
                    rows="2" 
                    placeholder="Ask Co-pilot or refine decision..." 
                    className="w-full bg-slate-900 border border-slate-700 rounded-lg p-2 text-xs focus:outline-none focus:border-teal-500 resize-none pr-10"
                  />
                  <button className="absolute right-2 bottom-2 text-teal-500 hover:text-teal-400">
                    <Zap size={16} fill="currentColor" />
                  </button>
                </div>
                <div className="mt-2 flex justify-between items-center">
                  <span className="text-[9px] text-slate-600 font-medium">Model: PAS-Underwriter-V2.5</span>
                  <div className="flex gap-2">
                    <span className="w-1.5 h-1.5 bg-teal-500 rounded-full"></span>
                    <span className="w-1.5 h-1.5 bg-teal-500 rounded-full"></span>
                    <span className="w-1.5 h-1.5 bg-teal-500 rounded-full animate-pulse"></span>
                  </div>
                </div>
              </div>
            </aside>
          </div>
        )}
      </main>
    </div>
  );
}
