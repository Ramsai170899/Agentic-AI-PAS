import React, { useState, useEffect } from 'react';
import { 
  Activity, 
  Search, 
  Brain, 
  FileText, 
  AlertTriangle, 
  CheckCircle2, 
  ChevronRight, 
  ShieldCheck, 
  Clock, 
  BarChart3,
  User,
  Zap,
  ArrowRightLeft,
  Settings,
  Database,
  Lock
} from 'lucide-react';

const App = () => {
  const [activeStep, setActiveStep] = useState(0);
  const [isProcessing, setIsProcessing] = useState(false);
  const [logs, setLogs] = useState([]);

  // Workflow steps configuration
  const workflowSteps = [
    {
      id: 'ingestion',
      title: 'Data Ingestion & Extraction',
      icon: <Database className="w-5 h-5" />,
      description: 'OCR & Semantic parsing of disparate sources (APS, Labs, Financials).',
      aiAction: 'Normalizing medical codes & financial statements...',
      status: 'complete'
    },
    {
      id: 'reasoning',
      title: 'Agentic Reasoning',
      icon: <Brain className="w-5 h-5" />,
      description: 'Cross-document discrepancy detection and risk signal weighting.',
      aiAction: 'Detecting undisclosed hypertension history from lab trends...',
      status: 'active'
    },
    {
      id: 'augmentation',
      title: 'Evidence Augmentation',
      icon: <Search className="w-5 h-5" />,
      description: 'Automated retrieval of MIB reports and reinsurance lookups.',
      aiAction: 'Checking reinsurance treaties for face amount >$5M...',
      status: 'pending'
    },
    {
      id: 'recommendation',
      title: 'Draft Recommendation',
      icon: <Zap className="w-5 h-5" />,
      description: 'Simulation of rating impacts (Table D vs. Flat Extra).',
      aiAction: 'Drafting rationale for Preferred Non-Smoker rating...',
      status: 'pending'
    },
    {
      id: 'human',
      title: 'Underwriter Adjudication',
      icon: <ShieldCheck className="w-5 h-5" />,
      description: 'Final human judgment, override capability, and ethics check.',
      aiAction: 'Awaiting Underwriter review of AI confidence metrics...',
      status: 'pending'
    }
  ];

  const simulationLogs = [
    { time: '10:02:01', msg: 'Started ingestion for Case #LI-9823-X', type: 'info' },
    { time: '10:02:05', msg: 'OCR extracted 42 health metrics from LabCorp PDF', type: 'success' },
    { time: '10:02:12', msg: 'Discrepancy: Declared weight vs. APS medical records (-15 lbs)', type: 'warning' },
    { time: '10:02:18', msg: 'Reinsurance query: Munich Re Auto-bind active', type: 'info' },
    { time: '10:02:25', msg: 'Projecting ROI for Table B rating over 20-year term', type: 'ai' },
  ];

  const handleNextStep = () => {
    if (activeStep < workflowSteps.length - 1) {
      setIsProcessing(true);
      setTimeout(() => {
        setActiveStep(prev => prev + 1);
        setIsProcessing(false);
      }, 1200);
    }
  };

  return (
    <div className="min-h-screen bg-[#0a0f18] text-slate-200 font-sans p-6 overflow-hidden flex flex-col">
      {/* Header */}
      <header className="flex items-center justify-between mb-8 border-b border-slate-800 pb-4">
        <div className="flex items-center gap-3">
          <div className="bg-teal-500 p-2 rounded-lg">
            <Activity className="text-white w-6 h-6" />
          </div>
          <div>
            <h1 className="text-xl font-bold tracking-tight">AGENTIC PAS WORKFLOW</h1>
            <p className="text-xs text-slate-500 uppercase tracking-widest">Enterprise Life Underwriting Engine v4.0</p>
          </div>
        </div>
        <div className="flex gap-4 items-center">
          <div className="flex items-center gap-2 px-3 py-1 bg-slate-900 border border-slate-800 rounded-full text-xs">
            <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
            AI Engine: Online
          </div>
          <Settings className="w-5 h-5 text-slate-500 cursor-pointer" />
        </div>
      </header>

      {/* Main Workflow View */}
      <div className="flex-1 grid grid-cols-12 gap-6">
        
        {/* Left: The Chain of Reasoning (Vertical Progress) */}
        <div className="col-span-3 space-y-4">
          <h3 className="text-sm font-semibold text-slate-400 mb-4 px-2">AGENT PIPELINE</h3>
          {workflowSteps.map((step, idx) => (
            <div 
              key={step.id} 
              className={`relative p-4 rounded-xl border transition-all duration-300 ${
                activeStep === idx 
                ? 'bg-slate-900/50 border-teal-500/50 shadow-[0_0_15px_rgba(20,184,166,0.1)]' 
                : activeStep > idx 
                ? 'border-slate-800 bg-transparent opacity-60' 
                : 'border-slate-800 bg-transparent opacity-30'
              }`}
            >
              <div className="flex items-start gap-3">
                <div className={`mt-1 p-2 rounded-md ${
                  activeStep === idx ? 'bg-teal-500 text-white' : 'bg-slate-800 text-slate-400'
                }`}>
                  {step.icon}
                </div>
                <div>
                  <h4 className="text-sm font-medium">{step.title}</h4>
                  <p className="text-[10px] text-slate-500 mt-1 leading-relaxed">{step.description}</p>
                </div>
              </div>
              {idx < workflowSteps.length - 1 && (
                <div className={`absolute left-7 -bottom-4 w-[1px] h-4 ${
                  activeStep > idx ? 'bg-teal-500' : 'bg-slate-800'
                }`}></div>
              )}
            </div>
          ))}
        </div>

        {/* Center: Live Action Pane (Simulation Environment) */}
        <div className="col-span-6 bg-slate-900/30 border border-slate-800 rounded-2xl flex flex-col relative overflow-hidden">
          <div className="p-4 border-b border-slate-800 flex justify-between items-center bg-slate-900/50">
            <div className="flex items-center gap-2">
              <Zap className="w-4 h-4 text-teal-400" />
              <span className="text-xs font-semibold uppercase">Active Case Simulation: #9823-X</span>
            </div>
            <div className="text-[10px] text-slate-500">Applicant: Jonathan D. | $2.5M Term Life</div>
          </div>

          {/* Visualizing the "Thinking" */}
          <div className="flex-1 p-8 flex flex-col items-center justify-center text-center">
            {isProcessing ? (
              <div className="space-y-6">
                <div className="relative">
                   <div className="w-24 h-24 rounded-full border-4 border-teal-500/20 border-t-teal-500 animate-spin"></div>
                   <Brain className="absolute inset-0 m-auto text-teal-500 w-8 h-8 animate-pulse" />
                </div>
                <div className="space-y-2">
                  <p className="text-lg font-medium text-white">{workflowSteps[activeStep].aiAction}</p>
                  <p className="text-xs text-slate-500 italic">Accessing structured and unstructured repositories...</p>
                </div>
              </div>
            ) : (
              <div className="w-full max-w-lg space-y-6 animate-in fade-in zoom-in duration-500">
                 {/* State-specific UI */}
                 {activeStep === 0 && (
                   <div className="grid grid-cols-2 gap-4">
                     <div className="bg-slate-800/50 p-4 rounded-lg border border-slate-700 text-left">
                        <FileText className="text-teal-400 mb-2 w-5 h-5" />
                        <div className="text-xs font-bold">APS RECORD</div>
                        <div className="h-1 w-full bg-slate-700 mt-2 rounded-full"><div className="w-full h-full bg-teal-500 rounded-full"></div></div>
                     </div>
                     <div className="bg-slate-800/50 p-4 rounded-lg border border-slate-700 text-left">
                        <BarChart3 className="text-teal-400 mb-2 w-5 h-5" />
                        <div className="text-xs font-bold">LAB RESULTS</div>
                        <div className="h-1 w-full bg-slate-700 mt-2 rounded-full"><div className="w-full h-full bg-teal-500 rounded-full"></div></div>
                     </div>
                   </div>
                 )}

                 {activeStep === 1 && (
                   <div className="bg-slate-800/50 p-6 rounded-xl border border-yellow-500/30 text-left">
                      <div className="flex items-center gap-2 text-yellow-500 mb-3">
                        <AlertTriangle className="w-5 h-5" />
                        <span className="text-sm font-bold">DISCREPANCY DETECTED</span>
                      </div>
                      <p className="text-sm text-slate-300">
                        Agent detected a conflict between <b>Application Item 14</b> (No Tobacco) and <b>Electronic Health Record</b> (Prescribed Nicotine Patch 2023).
                      </p>
                      <div className="mt-4 flex gap-2">
                        <span className="text-[10px] bg-yellow-500/20 text-yellow-500 px-2 py-1 rounded">Action: Flag for Underwriter</span>
                        <span className="text-[10px] bg-slate-700 px-2 py-1 rounded">Confidence: 94%</span>
                      </div>
                   </div>
                 )}

                 {activeStep === 3 && (
                   <div className="space-y-4">
                      <div className="text-left bg-teal-900/20 border border-teal-500/30 p-4 rounded-lg">
                        <div className="text-xs text-teal-500 font-bold mb-1">PROPOSED RATING</div>
                        <div className="text-2xl font-bold text-white">Table B (Standard)</div>
                        <p className="text-xs text-slate-400 mt-2">Due to BMI 32.1 and controlled Hypertension. Predicted Mortality: 125%</p>
                      </div>
                      <div className="flex gap-2 w-full">
                        <button className="flex-1 py-2 bg-teal-600 text-white rounded text-xs font-bold hover:bg-teal-500 transition-colors">ADOPT AS DRAFT</button>
                        <button className="flex-1 py-2 bg-slate-800 text-white rounded text-xs font-bold border border-slate-700">RE-SIMULATE</button>
                      </div>
                   </div>
                 )}

                 {activeStep === 4 && (
                   <div className="flex flex-col items-center">
                     <div className="w-16 h-16 bg-green-500/20 border border-green-500 rounded-full flex items-center justify-center mb-4">
                        <CheckCircle2 className="w-10 h-10 text-green-500" />
                     </div>
                     <h3 className="text-lg font-bold">Workflow Complete</h3>
                     <p className="text-sm text-slate-400 mt-2">AI Agent has generated the complete Underwriting Narrative and Decision Rationale. Ready for final Human Signature.</p>
                   </div>
                 )}

                 <div className="mt-10 pt-10 border-t border-slate-800/50">
                    <button 
                      onClick={handleNextStep}
                      disabled={activeStep === workflowSteps.length - 1}
                      className="px-8 py-3 bg-teal-500 text-white rounded-lg font-bold shadow-lg shadow-teal-500/20 hover:bg-teal-400 transition-all flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
                    >
                      {activeStep === workflowSteps.length - 1 ? 'Simulation Ended' : 'Trigger Next Agentic Phase'}
                      <ChevronRight className="w-4 h-4" />
                    </button>
                 </div>
              </div>
            )}
          </div>
          
          {/* Bottom Log Stream */}
          <div className="h-32 bg-black/40 border-t border-slate-800 p-3 font-mono text-[10px]">
            <div className="flex justify-between items-center mb-2 text-slate-500 uppercase tracking-tighter">
              <span>Agentic Execution Logs</span>
              <span>Filter: All Events</span>
            </div>
            <div className="space-y-1 overflow-y-auto max-h-20 scrollbar-hide">
              {simulationLogs.map((log, i) => (
                <div key={i} className="flex gap-4">
                  <span className="text-slate-600">[{log.time}]</span>
                  <span className={
                    log.type === 'warning' ? 'text-yellow-500' : 
                    log.type === 'success' ? 'text-green-500' : 
                    log.type === 'ai' ? 'text-teal-400 font-bold' : 'text-slate-400'
                  }>{log.msg}</span>
                </div>
              ))}
              {isProcessing && (
                <div className="flex gap-4 animate-pulse">
                  <span className="text-slate-600">[--:--:--]</span>
                  <span className="text-teal-400">Agent processing step {activeStep + 1}...</span>
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Right: Governance & Audit Pane */}
        <div className="col-span-3 space-y-6">
          <div className="bg-slate-900/50 border border-slate-800 rounded-xl p-4">
            <h4 className="text-xs font-bold text-slate-400 uppercase mb-4 flex items-center gap-2">
              <ShieldCheck className="w-4 h-4" />
              Explainability Matrix
            </h4>
            <div className="space-y-4">
              <div>
                <div className="flex justify-between text-[10px] mb-1">
                  <span>Logic Transparency</span>
                  <span className="text-teal-400">98%</span>
                </div>
                <div className="h-1 bg-slate-800 rounded-full overflow-hidden">
                  <div className="h-full bg-teal-500 w-[98%]"></div>
                </div>
              </div>
              <div>
                <div className="flex justify-between text-[10px] mb-1">
                  <span>Regulatory Compliance</span>
                  <span className="text-teal-400">100%</span>
                </div>
                <div className="h-1 bg-slate-800 rounded-full overflow-hidden">
                  <div className="h-full bg-teal-500 w-full"></div>
                </div>
              </div>
              <div>
                <div className="flex justify-between text-[10px] mb-1">
                  <span>Bias Mitigation</span>
                  <span className="text-blue-400">Protected</span>
                </div>
                <div className="h-1 bg-slate-800 rounded-full overflow-hidden">
                  <div className="h-full bg-blue-500 w-[90%]"></div>
                </div>
              </div>
            </div>
          </div>

          <div className="bg-slate-900/50 border border-slate-800 rounded-xl p-4">
             <h4 className="text-xs font-bold text-slate-400 uppercase mb-4 flex items-center gap-2">
              <Lock className="w-4 h-4" />
              Human-in-the-Loop
            </h4>
            <div className="text-[10px] text-slate-400 space-y-3">
              <div className="p-2 bg-slate-800 rounded flex gap-2 items-center">
                <div className="w-6 h-6 rounded bg-slate-700 flex items-center justify-center text-[8px] font-bold">AI</div>
                <span>Drafted Narrative</span>
                <div className="ml-auto flex gap-1">
                  <div className="w-3 h-3 rounded-full bg-green-500/20 border border-green-500 flex items-center justify-center"><CheckCircle2 className="w-2 h-2 text-green-500" /></div>
                </div>
              </div>
              <div className="p-2 bg-slate-800 rounded flex gap-2 items-center border border-teal-500/30">
                <div className="w-6 h-6 rounded bg-teal-500 flex items-center justify-center text-[8px] font-bold text-white">UW</div>
                <span>Pending Verification</span>
                <div className="ml-auto text-[8px] text-teal-400 animate-pulse">Required</div>
              </div>
              <div className="mt-4 pt-4 border-t border-slate-800">
                <p className="italic leading-relaxed">Agent has processed 14 documents. No autonomous decision was issued. All risk loadings are presented for underwriter approval.</p>
              </div>
            </div>
          </div>

          <div className="flex items-center gap-3 p-4 border border-slate-800 rounded-xl bg-slate-900/20">
             <div className="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center">
                <User className="text-slate-400 w-5 h-5" />
             </div>
             <div>
                <p className="text-xs font-bold">Assigned Underwriter</p>
                <p className="text-[10px] text-slate-500">Sr. Analyst Robert Chen</p>
             </div>
          </div>
        </div>

      </div>

      {/* Footer Info */}
      <footer className="mt-6 flex justify-between items-center text-[10px] text-slate-600 border-t border-slate-900 pt-4">
        <div>System: PAS-AGENT-PRO-11 | Secure Sandbox Environment</div>
        <div className="flex gap-4">
          <span>Audit Log ID: f92-0923-45a</span>
          <span>Regulatory Instance: NAIC-COMPLIANT-2024</span>
        </div>
      </footer>
    </div>
  );
};

export default App;
