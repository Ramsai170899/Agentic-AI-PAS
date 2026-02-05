import React, { useState, useEffect, useMemo } from 'react';
import { 
  LayoutDashboard, 
  FileText, 
  Search, 
  Bell, 
  User, 
  ShieldCheck, 
  AlertCircle, 
  TrendingUp, 
  Clock, 
  CheckCircle2, 
  XCircle, 
  MessageSquare, 
  Sparkles, 
  ChevronRight, 
  FileSearch, 
  Activity, 
  PlusCircle,
  Database,
  History,
  Scale
} from 'lucide-react';

// --- Mock Data ---
const QUEUE_DATA = [
  { id: 'POL-8821', applicant: 'Sarah Jenkins', type: 'Term Life', amount: '$1.2M', status: 'Priority', aiRisk: 42, flags: 2 },
  { id: 'POL-9012', applicant: 'Marcus Vane', type: 'Whole Life', amount: '$500k', status: 'Review', aiRisk: 15, flags: 0 },
  { id: 'POL-7734', applicant: 'Elena Rodriguez', type: 'Universal', amount: '$2.5M', status: 'Pending Info', aiRisk: 88, flags: 5 },
  { id: 'POL-8845', applicant: 'David Chen', type: 'Term Life', amount: '$750k', status: 'Priority', aiRisk: 31, flags: 1 },
];

const CASE_DETAILS = {
  id: 'POL-7734',
  applicant: {
    name: 'Elena Rodriguez',
    age: 44,
    occupation: 'Structural Engineer',
    income: '$185,000',
    hobbies: 'Scuba Diving (Advanced)',
  },
  medical: {
    bmi: 24.2,
    bloodPressure: '138/88',
    smoker: 'Non-Smoker',
    history: ['Gestational Diabetes (2018)', 'Mild Asthma'],
  },
  aiInsights: {
    score: 88,
    rationale: "High risk flagged due to discrepancy between 'No high-risk hobbies' on application and 'PADI Deep Diver' certification found in social/OCR sweep. Elevated BP trending near Stage 1 Hypertension.",
    summaries: {
      medical: "Applicant is generally healthy but shows a 12% increase in systolic pressure over 24 months. Asthma is well-controlled via inhaler.",
      financial: "Stable income; coverage amount (13.5x) is within standard 15x guidelines for age bracket."
    }
  }
};

// --- Components ---

const SidebarItem = ({ icon: Icon, label, active, onClick }) => (
  <button 
    onClick={onClick}
    className={`w-full flex items-center space-x-3 px-4 py-3 rounded-lg transition-all ${
      active ? 'bg-teal-700 text-white shadow-lg' : 'text-slate-400 hover:bg-slate-800 hover:text-slate-200'
    }`}
  >
    <Icon size={20} />
    <span className="font-medium">{label}</span>
  </button>
);

const StatCard = ({ label, value, trend, icon: Icon, color }) => (
  <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
    <div className="flex justify-between items-start">
      <div>
        <p className="text-slate-500 text-sm font-medium">{label}</p>
        <h3 className="text-2xl font-bold mt-1 text-slate-800">{value}</h3>
      </div>
      <div className={`p-2 rounded-lg ${color} bg-opacity-10 text-${color}-600`}>
        <Icon size={20} />
      </div>
    </div>
    <div className="mt-4 flex items-center text-xs text-slate-400">
      <TrendingUp size={12} className="mr-1 text-emerald-500" />
      <span className="text-emerald-500 font-semibold">{trend}</span>
      <span className="ml-1 text-slate-400">vs last month</span>
    </div>
  </div>
);

const App = () => {
  const [view, setView] = useState('dashboard'); // 'dashboard' or 'case'
  const [selectedCase, setSelectedCase] = useState(null);
  const [aiChat, setAiChat] = useState([
    { role: 'assistant', content: "Hello Underwriter. I've pre-analyzed Elena's file. I found a discrepancy in her avocation disclosure regarding deep-sea diving. Would you like me to draft a request for an Avocation Questionnaire?" }
  ]);

  const handleCaseClick = (item) => {
    setSelectedCase(item);
    setView('case');
  };

  return (
    <div className="flex h-screen bg-slate-50 text-slate-900 font-sans overflow-hidden">
      {/* Navigation Sidebar */}
      <aside className="w-64 bg-slate-900 flex flex-col p-4 shrink-0">
        <div className="flex items-center space-x-2 px-2 mb-8">
          <div className="w-8 h-8 bg-teal-500 rounded-lg flex items-center justify-center">
            <ShieldCheck className="text-white" size={20} />
          </div>
          <span className="text-white font-bold text-xl tracking-tight">LUMINA</span>
        </div>
        
        <nav className="flex-1 space-y-2">
          <SidebarItem icon={LayoutDashboard} label="Dashboard" active={view === 'dashboard'} onClick={() => setView('dashboard')} />
          <SidebarItem icon={FileText} label="My Queue" active={view === 'case'} onClick={() => setView('case')} />
          <SidebarItem icon={Activity} label="Analytics" />
          <SidebarItem icon={Database} label="Legacy Data" />
        </nav>

        <div className="mt-auto pt-4 border-t border-slate-800">
          <div className="flex items-center space-x-3 px-2">
            <div className="w-8 h-8 bg-slate-700 rounded-full flex items-center justify-center text-white text-xs font-bold">JD</div>
            <div className="flex-1">
              <p className="text-sm font-medium text-white">John Doe</p>
              <p className="text-xs text-slate-500">Senior Underwriter</p>
            </div>
          </div>
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="flex-1 flex flex-col overflow-hidden">
        {/* Header */}
        <header className="h-16 bg-white border-b border-slate-200 flex items-center justify-between px-8 shrink-0">
          <div className="flex items-center bg-slate-100 px-3 py-1.5 rounded-md w-96 border border-slate-200">
            <Search size={16} className="text-slate-400 mr-2" />
            <input 
              placeholder="Search policy, applicant name, or SSN..." 
              className="bg-transparent border-none outline-none text-sm w-full"
            />
          </div>
          <div className="flex items-center space-x-4">
            <button className="relative p-2 text-slate-500 hover:text-teal-600 transition-colors">
              <Bell size={20} />
              <span className="absolute top-1 right-1 w-2 h-2 bg-red-500 rounded-full border-2 border-white"></span>
            </button>
            <button className="bg-teal-600 hover:bg-teal-700 text-white px-4 py-2 rounded-lg text-sm font-semibold flex items-center transition-all shadow-md">
              <PlusCircle size={16} className="mr-2" />
              New Application
            </button>
          </div>
        </header>

        {/* Dynamic Viewport */}
        <div className="flex-1 overflow-y-auto p-8">
          {view === 'dashboard' ? (
            <div className="max-w-7xl mx-auto space-y-8">
              <div className="flex items-end justify-between">
                <div>
                  <h1 className="text-2xl font-bold text-slate-900 text-teal-900">Underwriter Command Center</h1>
                  <p className="text-slate-500">Welcome back. You have 4 priority cases requiring attention.</p>
                </div>
                <div className="text-right text-xs text-slate-400 font-mono">
                  REFRESHED: FEB 05, 2026 09:12 AM
                </div>
              </div>

              {/* KPI Widgets */}
              <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
                <StatCard label="Total Pipeline" value="142" trend="+12%" icon={FileText} color="blue" />
                <StatCard label="Avg. Turnaround" value="3.2 Days" trend="-0.5d" icon={Clock} color="teal" />
                <StatCard label="AI High-Risk Flags" value="18" trend="+4" icon={AlertCircle} color="amber" />
                <StatCard label="Approval Rate" value="74.2%" trend="+2.1%" icon={CheckCircle2} color="emerald" />
              </div>

              {/* Priority Queue Table */}
              <div className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
                <div className="px-6 py-4 border-b border-slate-200 flex justify-between items-center bg-slate-50/50">
                  <h2 className="font-bold text-slate-800">Priority Assessment Queue</h2>
                  <button className="text-teal-600 text-sm font-semibold hover:underline">View All Queue</button>
                </div>
                <table className="w-full text-left">
                  <thead className="bg-slate-50 text-slate-500 text-xs uppercase tracking-wider">
                    <tr>
                      <th className="px-6 py-3 font-medium">Policy ID</th>
                      <th className="px-6 py-3 font-medium">Applicant</th>
                      <th className="px-6 py-3 font-medium">Product</th>
                      <th className="px-6 py-3 font-medium">Face Amount</th>
                      <th className="px-6 py-3 font-medium">AI Risk Score</th>
                      <th className="px-6 py-3 font-medium">Status</th>
                      <th className="px-6 py-3 font-medium text-right">Action</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100">
                    {QUEUE_DATA.map((item) => (
                      <tr key={item.id} className="hover:bg-slate-50 transition-colors group">
                        <td className="px-6 py-4 font-mono text-sm text-slate-600">{item.id}</td>
                        <td className="px-6 py-4 font-semibold text-slate-800">{item.applicant}</td>
                        <td className="px-6 py-4 text-sm text-slate-600">{item.type}</td>
                        <td className="px-6 py-4 text-sm text-slate-800 font-medium">{item.amount}</td>
                        <td className="px-6 py-4">
                          <div className="flex items-center space-x-2">
                            <div className="flex-1 h-1.5 bg-slate-100 rounded-full w-16 overflow-hidden">
                              <div 
                                className={`h-full rounded-full ${item.aiRisk > 70 ? 'bg-red-500' : item.aiRisk > 40 ? 'bg-amber-500' : 'bg-emerald-500'}`}
                                style={{ width: `${item.aiRisk}%` }}
                              />
                            </div>
                            <span className="text-xs font-bold text-slate-600">{item.aiRisk}%</span>
                          </div>
                        </td>
                        <td className="px-6 py-4 text-xs font-bold uppercase">
                          <span className={`px-2 py-1 rounded-full ${
                            item.status === 'Priority' ? 'bg-red-100 text-red-700' : 
                            item.status === 'Review' ? 'bg-blue-100 text-blue-700' : 'bg-slate-100 text-slate-600'
                          }`}>
                            {item.status}
                          </span>
                        </td>
                        <td className="px-6 py-4 text-right">
                          <button 
                            onClick={() => handleCaseClick(item)}
                            className="text-slate-400 group-hover:text-teal-600 transition-colors"
                          >
                            <ChevronRight size={20} />
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          ) : (
            <div className="flex h-full space-x-6 max-w-[1600px] mx-auto">
              {/* Case Workspace Central Panel */}
              <div className="flex-1 space-y-6 overflow-y-auto pr-2">
                {/* Case Header */}
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-4">
                    <button onClick={() => setView('dashboard')} className="text-slate-400 hover:text-slate-600">
                      <ChevronRight className="rotate-180" size={24} />
                    </button>
                    <div>
                      <h1 className="text-2xl font-bold text-slate-900">{CASE_DETAILS.applicant.name}</h1>
                      <div className="flex items-center space-x-3 text-sm text-slate-500">
                        <span className="font-mono">{CASE_DETAILS.id}</span>
                        <span>•</span>
                        <span>Age {CASE_DETAILS.applicant.age}</span>
                        <span>•</span>
                        <span>{CASE_DETAILS.applicant.occupation}</span>
                      </div>
                    </div>
                  </div>
                  <div className="flex items-center space-x-3">
                    <button className="px-4 py-2 text-slate-600 bg-white border border-slate-200 rounded-lg text-sm font-semibold hover:bg-slate-50">
                      View Documents
                    </button>
                    <button className="px-4 py-2 bg-teal-600 text-white rounded-lg text-sm font-semibold hover:bg-teal-700 shadow-md">
                      Apply Rating
                    </button>
                  </div>
                </div>

                {/* Grid of Data Points */}
                <div className="grid grid-cols-2 gap-6">
                  {/* Medical Profile */}
                  <div className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                    <div className="flex items-center justify-between mb-4">
                      <h3 className="font-bold text-slate-800 flex items-center">
                        <Activity className="mr-2 text-teal-600" size={18} />
                        Biometric & Medical Profile
                      </h3>
                      <span className="text-[10px] bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded font-bold">OCR VERIFIED</span>
                    </div>
                    <div className="grid grid-cols-2 gap-y-4">
                      <div>
                        <p className="text-xs text-slate-400">BMI</p>
                        <p className="font-semibold">{CASE_DETAILS.medical.bmi}</p>
                      </div>
                      <div>
                        <p className="text-xs text-slate-400">Blood Pressure</p>
                        <p className="font-semibold">{CASE_DETAILS.medical.bloodPressure}</p>
                      </div>
                      <div>
                        <p className="text-xs text-slate-400">Tobacco Status</p>
                        <p className="font-semibold">{CASE_DETAILS.medical.smoker}</p>
                      </div>
                      <div>
                        <p className="text-xs text-slate-400">Primary Care</p>
                        <p className="font-semibold">Dr. A. Miller (LabCorp)</p>
                      </div>
                    </div>
                    <div className="mt-4 pt-4 border-t border-slate-100">
                      <p className="text-xs text-slate-400 mb-2 font-medium">MEDICAL HISTORY NOTES</p>
                      <div className="flex flex-wrap gap-2">
                        {CASE_DETAILS.medical.history.map(h => (
                          <span key={h} className="text-xs bg-slate-100 px-2 py-1 rounded text-slate-600">{h}</span>
                        ))}
                      </div>
                    </div>
                  </div>

                  {/* Financial & Avocation */}
                  <div className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
                    <div className="flex items-center justify-between mb-4">
                      <h3 className="font-bold text-slate-800 flex items-center">
                        <Database className="mr-2 text-blue-600" size={18} />
                        Financial & Risk Profile
                      </h3>
                    </div>
                    <div className="grid grid-cols-2 gap-y-4">
                      <div>
                        <p className="text-xs text-slate-400">Verified Income</p>
                        <p className="font-semibold text-emerald-600">{CASE_DETAILS.applicant.income}</p>
                      </div>
                      <div>
                        <p className="text-xs text-slate-400">Asset Valuation</p>
                        <p className="font-semibold">$1.4M (Estimated)</p>
                      </div>
                      <div className="col-span-2">
                        <p className="text-xs text-slate-400">Avocations Disclosed</p>
                        <p className="font-semibold text-red-600 flex items-center">
                          {CASE_DETAILS.applicant.hobbies}
                          <AlertCircle size={14} className="ml-2" />
                        </p>
                      </div>
                    </div>
                  </div>
                </div>

                {/* AI Evidence Chain / Audit Trail */}
                <div className="bg-slate-900 text-slate-300 p-6 rounded-xl border border-slate-800 shadow-lg">
                  <div className="flex items-center justify-between mb-4">
                    <h3 className="text-white font-bold flex items-center">
                      <Scale className="mr-2 text-teal-400" size={18} />
                      AI Evidence Reasoning Chain
                    </h3>
                    <div className="flex space-x-2">
                      <button className="text-[10px] border border-slate-700 px-2 py-1 rounded hover:bg-slate-800">Export Log</button>
                    </div>
                  </div>
                  <div className="space-y-4">
                    <div className="flex items-start space-x-3">
                      <div className="w-1.5 h-1.5 rounded-full bg-teal-500 mt-2"></div>
                      <p className="text-sm">
                        <span className="text-teal-400 font-bold">CROSS-CHECK:</span> Application hobby field says 'None', but OCR extracted 'Deep Sea Diving Certification' from document <span className="underline cursor-pointer">ID-992.pdf</span>.
                      </p>
                    </div>
                    <div className="flex items-start space-x-3 opacity-60">
                      <div className="w-1.5 h-1.5 rounded-full bg-slate-500 mt-2"></div>
                      <p className="text-sm">
                        <span className="text-slate-100 font-bold">MORTALITY MODEL:</span> Scuba certification level (Master) reduces basic hazard risk by 15% due to training experience.
                      </p>
                    </div>
                    <div className="flex items-start space-x-3">
                      <div className="w-1.5 h-1.5 rounded-full bg-amber-500 mt-2"></div>
                      <p className="text-sm">
                        <span className="text-amber-400 font-bold">FOLLOW-UP REQ:</span> System suggests ordering an APS (Attending Physician Statement) to clarify the 2018 Gestational Diabetes resolution.
                      </p>
                    </div>
                  </div>
                </div>
              </div>

              {/* Persistent AI Co-pilot Sidebar */}
              <div className="w-96 bg-white border border-slate-200 rounded-2xl flex flex-col shadow-xl overflow-hidden">
                <div className="p-4 bg-teal-900 text-white flex items-center justify-between">
                  <div className="flex items-center space-x-2">
                    <Sparkles size={18} className="text-teal-300" />
                    <span className="font-bold tracking-wide text-sm">AGENTIC AI CO-PILOT</span>
                  </div>
                  <div className="flex items-center space-x-2">
                    <span className="text-[10px] bg-teal-700 px-2 py-0.5 rounded">V.4.2</span>
                  </div>
                </div>

                <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-slate-50">
                  {aiChat.map((msg, idx) => (
                    <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                      <div className={`max-w-[85%] p-3 rounded-2xl text-sm shadow-sm ${
                        msg.role === 'user' 
                          ? 'bg-teal-600 text-white rounded-tr-none' 
                          : 'bg-white text-slate-800 border border-slate-200 rounded-tl-none'
                      }`}>
                        {msg.content}
                      </div>
                    </div>
                  ))}

                  {/* Suggestion Chips */}
                  <div className="space-y-2 mt-4">
                    <p className="text-[10px] text-slate-400 font-bold uppercase ml-1">Suggested Actions</p>
                    <button className="w-full text-left bg-white border border-slate-200 p-2.5 rounded-lg text-xs font-medium text-slate-700 hover:border-teal-500 hover:bg-teal-50 flex items-center">
                      <FileSearch size={14} className="mr-2 text-teal-600" />
                      Draft Avocation Questionnaire
                    </button>
                    <button className="w-full text-left bg-white border border-slate-200 p-2.5 rounded-lg text-xs font-medium text-slate-700 hover:border-teal-500 hover:bg-teal-50 flex items-center">
                      <Activity size={14} className="mr-2 text-teal-600" />
                      Calculate Premium Rating (Table B)
                    </button>
                    <button className="w-full text-left bg-white border border-slate-200 p-2.5 rounded-lg text-xs font-medium text-slate-700 hover:border-teal-500 hover:bg-teal-50 flex items-center">
                      <XCircle size={14} className="mr-2 text-red-600" />
                      Generate Declination Summary
                    </button>
                  </div>
                </div>

                {/* AI Input Area */}
                <div className="p-4 bg-white border-t border-slate-200">
                  <div className="relative">
                    <input 
                      placeholder="Ask the AI agent..." 
                      className="w-full bg-slate-100 border-none rounded-xl py-3 pl-4 pr-12 text-sm focus:ring-2 focus:ring-teal-500 outline-none"
                    />
                    <button className="absolute right-3 top-2.5 p-1 text-teal-600 hover:text-teal-800">
                      <MessageSquare size={20} />
                    </button>
                  </div>
                  <div className="flex justify-between items-center mt-3 px-1">
                    <span className="text-[10px] text-slate-400 italic flex items-center">
                      <Clock size={10} className="mr-1" /> Agent is monitoring case changes...
                    </span>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      </main>

      {/* Floating Action Bar (Contextual) */}
      <div className="fixed bottom-6 left-1/2 -translate-x-1/2 bg-slate-900/95 backdrop-blur-md text-white px-6 py-3 rounded-full flex items-center space-x-6 shadow-2xl border border-slate-700">
        <div className="flex items-center space-x-2 pr-6 border-r border-slate-700">
          <div className={`w-3 h-3 rounded-full bg-red-500 animate-pulse`}></div>
          <span className="text-xs font-bold uppercase tracking-wider">Risk Level: High</span>
        </div>
        <div className="flex items-center space-x-4">
          <button className="text-xs font-bold hover:text-teal-400 transition-colors">REQUEST EVIDENCE</button>
          <button className="text-xs font-bold hover:text-teal-400 transition-colors">MODIFY TERMS</button>
          <button className="bg-teal-500 hover:bg-teal-400 text-slate-900 px-4 py-1.5 rounded-full text-xs font-bold transition-all transform active:scale-95">
            FINAL DECISION
          </button>
        </div>
      </div>
    </div>
  );
};

export default App;
