import React, { useState, useEffect, useMemo } from 'react';
import { 
  LayoutDashboard, 
  FileText, 
  Activity, 
  ShieldCheck, 
  AlertTriangle, 
  Search, 
  MessageSquare, 
  ChevronRight, 
  ExternalLink, 
  Cpu, 
  FileSearch, 
  Stethoscope, 
  DollarSign, 
  CheckCircle2, 
  History,
  Terminal,
  Zap
} from 'lucide-react';

const App = () => {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [selectedCase, setSelectedCase] = useState(null);
  const [isAiProcessing, setIsAiProcessing] = useState(false);
  const [aiInsightLevel, setAiInsightLevel] = useState('standard');

  // Mock Data: Prioritized Queue
  const cases = [
    { id: 'L-88291', name: 'Jonathan Thorne', amount: '$2,500,000', risk: 'High', status: 'In Review', urgency: 92, signals: ['Medical Trend', 'Financial Gap'] },
    { id: 'L-88304', name: 'Elena Rodriguez', amount: '$500,000', risk: 'Low', status: 'Pending Evidence', urgency: 45, signals: ['Clean Lab'] },
    { id: 'L-88312', name: 'Marcus Chen', amount: '$1,200,000', risk: 'Medium', status: 'New', urgency: 78, signals: ['Avocation Flag'] },
  ];

  const handleCaseSelect = (item) => {
    setIsAiProcessing(true);
    setTimeout(() => {
      setSelectedCase(item);
      setIsAiProcessing(false);
      setActiveTab('case-workspace');
    }, 800);
  };

  return (
    <div className="flex h-screen w-full bg-[#f8fafc] text-slate-900 font-sans overflow-hidden">
      {/* GLOBAL NAVIGATION SIDEBAR */}
      <aside className="w-16 flex flex-col items-center py-6 bg-[#0f172a] text-white space-y-8 border-r border-slate-800">
        <div className="p-2 bg-teal-500 rounded-lg">
          <ShieldCheck size={24} />
        </div>
        <nav className="flex flex-col space-y-6">
          <button onClick={() => setActiveTab('dashboard')} className={`p-2 rounded-lg transition ${activeTab === 'dashboard' ? 'bg-teal-500/20 text-teal-400' : 'text-slate-400 hover:text-white'}`}>
            <LayoutDashboard size={22} />
          </button>
          <button onClick={() => setActiveTab('case-workspace')} className={`p-2 rounded-lg transition ${activeTab === 'case-workspace' ? 'bg-teal-500/20 text-teal-400' : 'text-slate-400 hover:text-white'}`}>
            <FileText size={22} />
          </button>
          <button className="text-slate-400 hover:text-white p-2">
            <Activity size={22} />
          </button>
          <button className="text-slate-400 hover:text-white p-2">
            <History size={22} />
          </button>
        </nav>
        <div className="mt-auto pb-4">
          <div className="w-8 h-8 rounded-full bg-slate-700 flex items-center justify-center text-xs font-bold">JD</div>
        </div>
      </aside>

      {/* MAIN CONTENT AREA */}
      <main className="flex-1 flex flex-col overflow-hidden">
        {/* HEADER */}
        <header className="h-14 bg-white border-b border-slate-200 flex items-center justify-between px-6 shrink-0">
          <div className="flex items-center space-x-4">
            <h1 className="font-bold text-slate-800 tracking-tight uppercase text-sm">Underwriting OS v4.2</h1>
            <span className="text-slate-300">|</span>
            <div className="flex items-center space-x-2 text-xs font-medium text-slate-500">
              <span className="w-2 h-2 rounded-full bg-green-500"></span>
              <span>Agentic Core Online</span>
            </div>
          </div>
          <div className="flex items-center space-x-4">
            <div className="relative">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" size={14} />
              <input 
                placeholder="Search policy, SSN, or Lab ID..." 
                className="pl-9 pr-4 py-1.5 bg-slate-100 border-none rounded-md text-xs w-64 focus:ring-1 focus:ring-teal-500 outline-none transition-all"
              />
            </div>
          </div>
        </header>

        {activeTab === 'dashboard' ? (
          <DashboardView cases={cases} onSelect={handleCaseSelect} />
        ) : (
          <CaseWorkspace selectedCase={selectedCase} isAiProcessing={isAiProcessing} />
        )}
      </main>
    </div>
  );
};

const DashboardView = ({ cases, onSelect }) => (
  <div className="flex-1 overflow-y-auto p-6 space-y-6">
    {/* KPI ROWS */}
    <div className="grid grid-cols-4 gap-4">
      {[
        { label: 'Active Queue', val: '24', trend: '+2', color: 'text-slate-800' },
        { label: 'Avg Cycle Time', val: '4.2d', trend: '-0.5d', color: 'text-teal-600' },
        { label: 'High Priority Alerts', val: '07', trend: '!', color: 'text-rose-600' },
        { label: 'AI Throughput', val: '88%', trend: '+4%', color: 'text-blue-600' },
      ].map((kpi, i) => (
        <div key={i} className="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
          <div className="text-[10px] font-bold text-slate-400 uppercase tracking-wider mb-1">{kpi.label}</div>
          <div className="flex items-end justify-between">
            <div className={`text-2xl font-bold ${kpi.color}`}>{kpi.val}</div>
            <div className="text-[10px] font-bold bg-slate-100 px-2 py-0.5 rounded text-slate-500">{kpi.trend}</div>
          </div>
        </div>
      ))}
    </div>

    {/* CASE QUEUE TABLE */}
    <div className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
      <div className="p-4 border-b border-slate-100 flex items-center justify-between">
        <h3 className="font-bold text-slate-700 text-sm flex items-center gap-2">
          <Terminal size={16} className="text-teal-500" />
          AI-Prioritized Underwriting Queue
        </h3>
        <div className="flex gap-2">
          <button className="text-[10px] font-bold uppercase tracking-tight px-3 py-1 bg-slate-50 text-slate-500 rounded border border-slate-200">Export</button>
          <button className="text-[10px] font-bold uppercase tracking-tight px-3 py-1 bg-[#0f172a] text-white rounded shadow-lg shadow-blue-900/20">Refresh Signals</button>
        </div>
      </div>
      <table className="w-full text-left text-sm">
        <thead className="bg-slate-50 border-b border-slate-100">
          <tr>
            <th className="px-6 py-3 font-semibold text-slate-500 text-[11px] uppercase">Urgency Score</th>
            <th className="px-6 py-3 font-semibold text-slate-500 text-[11px] uppercase">Applicant</th>
            <th className="px-6 py-3 font-semibold text-slate-500 text-[11px] uppercase">Face Amount</th>
            <th className="px-6 py-3 font-semibold text-slate-500 text-[11px] uppercase">Status / Phase</th>
            <th className="px-6 py-3 font-semibold text-slate-500 text-[11px] uppercase">AI Signals</th>
            <th className="px-6 py-3"></th>
          </tr>
        </thead>
        <tbody className="divide-y divide-slate-100">
          {cases.map((item) => (
            <tr key={item.id} className="hover:bg-slate-50/80 transition cursor-pointer group" onClick={() => onSelect(item)}>
              <td className="px-6 py-4">
                <div className="flex items-center gap-3">
                  <div className={`w-1 h-8 rounded-full ${item.urgency > 80 ? 'bg-rose-500 shadow-sm shadow-rose-200' : 'bg-teal-500'}`}></div>
                  <span className="font-mono font-bold text-slate-700">{item.urgency}%</span>
                </div>
              </td>
              <td className="px-6 py-4">
                <div className="font-semibold text-slate-800">{item.name}</div>
                <div className="text-[11px] text-slate-400">{item.id}</div>
              </td>
              <td className="px-6 py-4 font-medium text-slate-600">{item.amount}</td>
              <td className="px-6 py-4">
                <span className="px-2 py-1 bg-slate-100 text-slate-600 rounded-md text-[10px] font-bold uppercase tracking-tighter">
                  {item.status}
                </span>
              </td>
              <td className="px-6 py-4">
                <div className="flex gap-1">
                  {item.signals.map(s => (
                    <span key={s} className="px-1.5 py-0.5 border border-amber-200 bg-amber-50 text-amber-700 text-[9px] font-bold rounded flex items-center gap-1">
                      <Zap size={8} /> {s}
                    </span>
                  ))}
                </div>
              </td>
              <td className="px-6 py-4 text-right">
                <ChevronRight size={18} className="text-slate-300 group-hover:text-teal-500 transition-colors inline" />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  </div>
);

const CaseWorkspace = ({ selectedCase, isAiProcessing }) => {
  if (isAiProcessing) return (
    <div className="flex-1 flex flex-col items-center justify-center bg-white">
      <div className="w-12 h-12 border-4 border-teal-500/20 border-t-teal-500 rounded-full animate-spin mb-4"></div>
      <p className="text-xs font-bold text-slate-500 uppercase tracking-widest animate-pulse">
        Agentic AI: Synthesizing medical & financial evidence...
      </p>
    </div>
  );

  return (
    <div className="flex-1 flex overflow-hidden">
      {/* CENTRAL COCKPIT (HUMAN-CENTRIC DATA) */}
      <section className="flex-1 overflow-y-auto bg-white border-r border-slate-200 flex flex-col">
        {/* CASE HEADER */}
        <div className="p-6 border-b border-slate-100 flex items-start justify-between bg-slate-50/50">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <h2 className="text-xl font-bold text-slate-800">{selectedCase?.name || 'Applicant Workspace'}</h2>
              <span className="px-2 py-0.5 bg-blue-100 text-blue-700 text-[10px] font-bold rounded uppercase">Standard Non-Smoker</span>
            </div>
            <div className="flex items-center gap-4 text-xs text-slate-500">
              <span className="flex items-center gap-1"><FileText size={12}/> Policy: {selectedCase?.id || 'N/A'}</span>
              <span className="flex items-center gap-1"><Activity size={12}/> Age: 42</span>
              <span className="flex items-center gap-1"><DollarSign size={12}/> Requested: {selectedCase?.amount || 'N/A'}</span>
            </div>
          </div>
          <div className="flex gap-2">
             <button className="px-4 py-2 bg-white border border-slate-200 text-slate-600 rounded-lg text-xs font-bold hover:bg-slate-50 shadow-sm transition">Manual Evidence Request</button>
             <button className="px-4 py-2 bg-[#0f172a] text-white rounded-lg text-xs font-bold shadow-lg shadow-blue-900/30 hover:bg-slate-800 transition">Execute Decision</button>
          </div>
        </div>

        {/* WORKSPACE SECTIONS */}
        <div className="p-6 space-y-8">
          {/* MEDICAL SECTION */}
          <div>
            <div className="flex items-center justify-between mb-4 border-b border-slate-100 pb-2">
              <h4 className="font-bold text-slate-800 text-sm flex items-center gap-2 uppercase tracking-tight">
                <Stethoscope size={16} className="text-teal-600" /> Medical & Laboratory Data
              </h4>
              <span className="text-[10px] text-teal-600 font-bold bg-teal-50 px-2 py-0.5 rounded">AI Verified 2m ago</span>
            </div>
            <div className="grid grid-cols-3 gap-4">
              <LabCard label="HbA1c" value="5.8%" status="Normal" />
              <LabCard label="Total Chol" value="230 mg/dL" status="Elevated" highlighted />
              <LabCard label="BP (Systolic)" value="142" status="Borderline" highlighted />
            </div>
            <div className="mt-4 p-4 bg-slate-50 rounded-lg border border-slate-100">
              <p className="text-[11px] leading-relaxed text-slate-600">
                <span className="font-bold text-slate-800 uppercase mr-2 text-[10px]">History:</span> 
                Patient reported mild hypertension in 2021 application. Current readings show improvement but remain above optimal target. Smoking status confirmed Negative via Cotinine screen.
              </p>
            </div>
          </div>

          {/* FINANCIAL SECTION */}
          <div>
            <div className="flex items-center justify-between mb-4 border-b border-slate-100 pb-2">
              <h4 className="font-bold text-slate-800 text-sm flex items-center gap-2 uppercase tracking-tight">
                <DollarSign size={16} className="text-teal-600" /> Financial Justification
              </h4>
            </div>
            <div className="bg-white border border-slate-200 rounded-xl overflow-hidden">
               <div className="grid grid-cols-2 divide-x divide-slate-100">
                  <div className="p-4">
                    <div className="text-[10px] font-bold text-slate-400 uppercase mb-2">Income Verification</div>
                    <div className="flex items-center justify-between">
                      <span className="text-sm font-medium text-slate-700">Reported: $450k/yr</span>
                      <span className="text-[10px] bg-green-100 text-green-700 px-1.5 py-0.5 rounded font-bold">Tax Verified</span>
                    </div>
                  </div>
                  <div className="p-4">
                    <div className="text-[10px] font-bold text-slate-400 uppercase mb-2">Total In-Force</div>
                    <div className="text-sm font-medium text-slate-700">$5,200,000 across 3 carriers</div>
                  </div>
               </div>
            </div>
          </div>

          {/* DOCUMENT HUB PREVIEW */}
          <div className="bg-slate-900 rounded-xl p-4 text-white">
            <div className="flex items-center justify-between mb-3">
              <span className="text-[11px] font-bold uppercase tracking-widest text-slate-400">Digital Evidence Hub</span>
              <ExternalLink size={14} className="text-slate-400 cursor-pointer" />
            </div>
            <div className="space-y-2">
              <div className="flex items-center justify-between p-2 bg-slate-800/50 rounded-md border border-slate-700 hover:border-teal-500/50 transition cursor-pointer">
                <div className="flex items-center gap-3">
                  <div className="p-2 bg-rose-500/20 text-rose-400 rounded">PDF</div>
                  <span className="text-xs font-medium">Attending Physician Statement (St. Jude Medical)</span>
                </div>
                <span className="text-[10px] text-slate-500 italic">Analyzed by AI</span>
              </div>
              <div className="flex items-center justify-between p-2 bg-slate-800/50 rounded-md border border-slate-700">
                <div className="flex items-center gap-3">
                  <div className="p-2 bg-blue-500/20 text-blue-400 rounded">IMG</div>
                  <span className="text-xs font-medium">Lab Corp Chemistry Results - 10/24/2023</span>
                </div>
                <span className="text-[10px] text-teal-400 font-bold">OCR Sync Complete</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* AGENTIC AI CO-PILOT SIDEBAR */}
      <aside className="w-[380px] bg-[#f1f5f9] border-l border-slate-200 flex flex-col">
        <div className="p-4 bg-white border-b border-slate-200">
          <div className="flex items-center gap-2 mb-4">
            <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-teal-400 to-blue-600 flex items-center justify-center text-white shadow-md">
              <Cpu size={18} />
            </div>
            <div>
              <h3 className="font-bold text-slate-800 text-sm">Agentic Co-pilot</h3>
              <p className="text-[10px] text-slate-500 font-medium uppercase tracking-tighter">Autonomous Reasoning Layer</p>
            </div>
          </div>
          
          <div className="bg-teal-50 border border-teal-100 rounded-lg p-3">
            <div className="flex items-center justify-between mb-2">
              <span className="text-[11px] font-bold text-teal-800 flex items-center gap-1">
                <ShieldCheck size={14} /> Risk Recommendation
              </span>
              <span className="text-[11px] font-black text-teal-600 uppercase">96% Conf</span>
            </div>
            <p className="text-xs text-teal-900 leading-relaxed font-medium">
              Recommend <span className="underline decoration-teal-400 font-bold underline-offset-2">Standard Plus</span>. Elevated BMI and BP are mitigated by long-term stability and consistent medication adherence verified via Pharmacy Records.
            </p>
          </div>
        </div>

        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {/* ACTIVE DISCREPANCY DETECTION */}
          <div className="space-y-2">
            <h5 className="text-[10px] font-bold text-slate-400 uppercase tracking-widest px-1">Evidence Discrepancies</h5>
            <div className="bg-white border-l-4 border-rose-500 p-3 rounded shadow-sm">
              <div className="flex items-center gap-2 text-rose-700 font-bold text-xs mb-1">
                <AlertTriangle size={14} /> Mismatch Flag: Smoking
              </div>
              <p className="text-[11px] text-slate-600 leading-normal">
                Application: "Non-Smoker". 2021 MIB Code indicates history of nicotine usage. <span className="text-teal-600 font-bold cursor-pointer">Draft Clarification Letter?</span>
              </p>
            </div>
          </div>

          {/* REASONING CHAIN */}
          <div className="space-y-2">
            <h5 className="text-[10px] font-bold text-slate-400 uppercase tracking-widest px-1">Reasoning Chain</h5>
            <div className="bg-slate-800 rounded-lg p-4 font-mono text-[10px] text-slate-300 space-y-2 overflow-hidden">
               <div className="flex gap-2">
                 <span className="text-teal-500">[0ms]</span> Initializing ingestion protocol...
               </div>
               <div className="flex gap-2">
                 <span className="text-teal-500">[42ms]</span> Analyzing APS (v.2.1) - PDF Segment 4/12
               </div>
               <div className="flex gap-2 items-center">
                 <span className="text-teal-500">[110ms]</span> <CheckCircle2 size={10} className="text-green-400" /> Lab values normalized to actuarial table.
               </div>
               <div className="flex gap-2">
                 <span className="text-teal-500">[240ms]</span> Cross-referencing Rx Profile with reported comorbidities...
               </div>
               <div className="animate-pulse flex gap-2">
                 <span className="text-blue-400">[*]</span> Monitoring for new digital evidence...
               </div>
            </div>
          </div>

          {/* AUTO-DRAFTING ACTIONS */}
          <div className="pt-4">
            <h5 className="text-[10px] font-bold text-slate-400 uppercase tracking-widest px-1 mb-2">Automated Actions</h5>
            <div className="grid grid-cols-2 gap-2">
              <button className="flex flex-col items-center justify-center p-3 bg-white border border-slate-200 rounded-lg hover:border-teal-500 hover:text-teal-600 transition group text-center">
                <FileSearch size={18} className="text-slate-400 group-hover:text-teal-500 mb-2" />
                <span className="text-[10px] font-bold leading-tight uppercase">Draft APS Summary</span>
              </button>
              <button className="flex flex-col items-center justify-center p-3 bg-white border border-slate-200 rounded-lg hover:border-teal-500 hover:text-teal-600 transition group text-center">
                <MessageSquare size={18} className="text-slate-400 group-hover:text-teal-500 mb-2" />
                <span className="text-[10px] font-bold leading-tight uppercase">Draft Offer Note</span>
              </button>
            </div>
          </div>
        </div>

        {/* AI FEEDBACK LOOP / GOVERNANCE */}
        <div className="p-4 bg-slate-200/50 border-t border-slate-300">
          <div className="text-[10px] font-bold text-slate-500 uppercase mb-2">Human-in-the-Loop Feedback</div>
          <div className="flex gap-2">
            <button className="flex-1 py-1.5 bg-white text-slate-600 text-[10px] font-bold rounded border border-slate-300 hover:bg-teal-50 hover:border-teal-200 transition">Confirm AI Reasoning</button>
            <button className="flex-1 py-1.5 bg-white text-slate-600 text-[10px] font-bold rounded border border-slate-300 hover:bg-rose-50 hover:border-rose-200 transition">Adjust / Override</button>
          </div>
        </div>
      </aside>
    </div>
  );
};

const LabCard = ({ label, value, status, highlighted = false }) => (
  <div className={`p-3 rounded-lg border ${highlighted ? 'bg-amber-50 border-amber-200 shadow-sm' : 'bg-white border-slate-100'}`}>
    <div className="text-[10px] font-bold text-slate-400 uppercase mb-1">{label}</div>
    <div className="flex items-center justify-between">
      <span className="text-sm font-bold text-slate-800">{value}</span>
      <span className={`text-[9px] font-black uppercase px-1.5 py-0.5 rounded ${status === 'Normal' ? 'bg-green-100 text-green-700' : 'bg-amber-100 text-amber-700'}`}>
        {status}
      </span>
    </div>
  </div>
);

export default App;
