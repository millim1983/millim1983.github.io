
---
title: "열분해 공정 모니터링 및 통합제어용 온데바이스 ai기반소프트 센서팩 및 제어시스템"
date: 2026-02-02
categories: [blog]
tags: [html]
---

<!-- 여기부터 HTML 그대로 붙여넣기 -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>On-Device AI Soft Sensor for Pyrolysis Control</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Plotly.js -->
    <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
    
    <!-- Palette: Electric Intelligence -->
    <!-- Primary: #2563EB (Royal Blue), Secondary: #06B6D4 (Cyan), Accent: #7C3AED (Violet) -->
    
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

        body {
            font-family: 'Inter', sans-serif;
            background-color: #F8FAFC; /* Slate 50 */
            color: #1E293B; /* Slate 800 */
        }

        /* Chart Container Styling - Mandatory */
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 100%; /* Parent controls width, but max-w can be set here if needed */
            margin-left: auto;
            margin-right: auto;
            height: 300px; /* Base height for mobile */
            max-height: 400px;
            overflow: hidden; /* Prevent overflow */
        }

        /* Responsive adjustments for chart height */
        @media (min-width: 768px) {
            .chart-container {
                height: 350px;
            }
        }
        @media (min-width: 1024px) {
            .chart-container {
                height: 400px;
            }
        }

        /* Custom Gradients */
        .bg-gradient-vibrant {
            background: linear-gradient(135deg, #2563EB 0%, #06B6D4 100%);
        }
        .text-gradient-vibrant {
            background: linear-gradient(135deg, #2563EB 0%, #7C3AED 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Card Hover Effects */
        .card-hover {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .card-hover:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.15), 0 8px 10px -6px rgba(37, 99, 235, 0.1);
        }

        /* Custom diagram connectors */
        .connector-line {
            width: 2px;
            background-color: #CBD5E1; /* Slate 300 */
        }
    </style>
    <!-- 
        NARRATIVE PLAN:
        1. Introduction: Define the High-Tech Mission (On-Device AI for Pyrolysis).
        2. The Problem: Limitations of Physical Sensors in extreme environments.
        3. The Solution: The "Soft Sensor Pack" architecture (Visual Diagram).
        4. Core KPIs: Accuracy & Efficiency Targets (Chart.js Donut & Bar).
        5. Advanced Control: 3D Visualization of Optimization (Plotly).
        6. Impact: Energy & Carbon Neutrality (Chart.js Pie).
        7. Timeline: Project Roadmap (HTML Timeline).
        
        PALETTE: "Electric Intelligence" - Focusing on Blue, Cyan, and Violet to convey 
        Smart Manufacturing, AI, and Clean Energy.
        
        SVG / MERMAID JS CHECK:
        - No SVG tags used.
        - No Mermaid JS libraries imported or used.
        - Diagrams implemented via HTML/CSS layout.
    -->
</head>
<body class="antialiased">

    <!-- HERO SECTION -->
    <header class="bg-gradient-vibrant text-white py-16 px-4 sm:px-6 lg:px-8 shadow-xl">
        <div class="max-w-7xl mx-auto text-center">
            <div class="inline-block bg-white/20 backdrop-blur-md rounded-full px-4 py-1 mb-4 border border-white/30">
                <span class="font-semibold tracking-wider text-sm uppercase">2026 Industrial Convergence Project</span>
            </div>
            <h1 class="text-4xl md:text-6xl font-extrabold mb-4 leading-tight">
                On-Device AI Soft Sensor
            </h1>
            <h2 class="text-xl md:text-2xl font-light text-blue-100 mb-8 max-w-3xl mx-auto">
                Revolutionizing Organic Material Pyrolysis with Intelligent Process Control
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl mx-auto mt-12 text-left">
                <div class="bg-white/10 backdrop-blur-sm p-4 rounded-lg border border-white/20">
                    <p class="text-blue-200 text-xs uppercase font-bold tracking-widest mb-1">Target</p>
                    <p class="font-bold text-lg">Pyrolysis Process Control</p>
                </div>
                <div class="bg-white/10 backdrop-blur-sm p-4 rounded-lg border border-white/20">
                    <p class="text-blue-200 text-xs uppercase font-bold tracking-widest mb-1">Technology</p>
                    <p class="font-bold text-lg">Virtual Soft Sensors</p>
                </div>
                <div class="bg-white/10 backdrop-blur-sm p-4 rounded-lg border border-white/20">
                    <p class="text-blue-200 text-xs uppercase font-bold tracking-widest mb-1">Goal</p>
                    <p class="font-bold text-lg">Carbon Neutrality</p>
                </div>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-24">

        <!-- SECTION 1: THE CHALLENGE -->
        <section>
            <div class="text-center mb-12">
                <h3 class="text-3xl font-bold text-slate-800 mb-4">Why Soft Sensors?</h3>
                <p class="text-slate-600 max-w-2xl mx-auto">
                    Traditional manufacturing faces a critical bottleneck in the pyrolysis process. 
                    Extreme conditions make physical monitoring unreliable, leading to inefficiency.
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- Problem Card -->
                <div class="bg-white rounded-2xl shadow-lg p-8 border-l-8 border-red-500 card-hover">
                    <div class="flex items-center mb-6">
                        <div class="w-12 h-12 rounded-full bg-red-100 flex items-center justify-center text-red-600 font-bold text-xl mr-4">!</div>
                        <h4 class="text-2xl font-bold text-slate-800">Physical Sensor Limitations</h4>
                    </div>
                    <ul class="space-y-4 text-slate-600">
                        <li class="flex items-start">
                            <span class="mr-2 mt-1 text-red-500">&#10008;</span>
                            <span>High temperatures and pressures degrade sensor lifespan rapidly.</span>
                        </li>
                        <li class="flex items-start">
                            <span class="mr-2 mt-1 text-red-500">&#10008;</span>
                            <span>Real-time analysis of complex gas compositions (H2, CxHy) is difficult.</span>
                        </li>
                        <li class="flex items-start">
                            <span class="mr-2 mt-1 text-red-500">&#10008;</span>
                            <span>Inability to measure internal reactor states directly leads to energy waste.</span>
                        </li>
                    </ul>
                </div>

                <!-- Solution Card -->
                <div class="bg-white rounded-2xl shadow-lg p-8 border-l-8 border-emerald-500 card-hover">
                    <div class="flex items-center mb-6">
                        <div class="w-12 h-12 rounded-full bg-emerald-100 flex items-center justify-center text-emerald-600 font-bold text-xl mr-4">&#10003;</div>
                        <h4 class="text-2xl font-bold text-slate-800">AI Soft Sensor Solution</h4>
                    </div>
                    <ul class="space-y-4 text-slate-600">
                        <li class="flex items-start">
                            <span class="mr-2 mt-1 text-emerald-500">&#10003;</span>
                            <span><strong>Virtual Sensing:</strong> Estimates internal states using external data (Time, Temp, Pressure).</span>
                        </li>
                        <li class="flex items-start">
                            <span class="mr-2 mt-1 text-emerald-500">&#10003;</span>
                            <span><strong>On-Device AI:</strong> Processes data locally for real-time control without cloud latency.</span>
                        </li>
                        <li class="flex items-start">
                            <span class="mr-2 mt-1 text-emerald-500">&#10003;</span>
                            <span><strong>Multi-Variable Pack:</strong> Simultaneously predicts Quality, Gas Specs, and Carbon Credits.</span>
                        </li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- SECTION 2: SYSTEM ARCHITECTURE (Flow Diagram) -->
        <section class="bg-slate-50 rounded-3xl p-8 md:p-12 border border-slate-200">
            <div class="text-center mb-12">
                <span class="text-blue-600 font-bold tracking-wider uppercase text-sm">Technology Stack</span>
                <h3 class="text-3xl font-bold text-slate-800 mt-2">The Soft Sensor Pack Architecture</h3>
                <p class="text-slate-600 mt-4 max-w-3xl mx-auto">
                    A closed-loop system where physical data feeds an On-Device AI, generating virtual insights 
                    that drive process optimization and carbon accounting.
                </p>
            </div>

            <!-- HTML/CSS Diagram -->
            <div class="flex flex-col md:flex-row items-center justify-center gap-4 relative">
                
                <!-- Step 1: Input -->
                <div class="w-full md:w-1/4 bg-white p-6 rounded-xl shadow-md border-t-4 border-slate-400 text-center z-10">
                    <div class="text-4xl mb-4">⚙️</div>
                    <h5 class="font-bold text-lg mb-2">Process Inputs</h5>
                    <p class="text-sm text-slate-500">Temperature, Pressure, Time, Material Feed</p>
                </div>

                <!-- Connector -->
                <div class="hidden md:block text-slate-300 text-3xl">&#10145;</div>
                <div class="md:hidden text-slate-300 text-3xl rotate-90 my-2">&#10145;</div>

                <!-- Step 2: Core AI -->
                <div class="w-full md:w-1/4 bg-white p-6 rounded-xl shadow-xl border-t-4 border-blue-600 text-center z-10 transform scale-105">
                    <div class="text-4xl mb-4">🧠</div>
                    <h5 class="font-bold text-lg mb-2 text-blue-700">On-Device AI Model</h5>
                    <p class="text-sm text-slate-500">Real-time Simulation & Deep Learning Inference</p>
                </div>

                <!-- Connector -->
                <div class="hidden md:block text-slate-300 text-3xl">&#10145;</div>
                <div class="md:hidden text-slate-300 text-3xl rotate-90 my-2">&#10145;</div>

                <!-- Step 3: Soft Sensor Pack -->
                <div class="w-full md:w-1/4 bg-white p-6 rounded-xl shadow-md border-t-4 border-cyan-500 text-center z-10">
                    <div class="text-4xl mb-4">📊</div>
                    <h5 class="font-bold text-lg mb-2 text-cyan-700">Soft Sensor Pack</h5>
                    <ul class="text-xs text-left list-disc pl-4 text-slate-600 space-y-1">
                        <li>Gas Characteristics</li>
                        <li>Thermal Intensity</li>
                        <li>Quality Yield</li>
                        <li>Carbon Credit</li>
                    </ul>
                </div>
            </div>
            
            <!-- Feedback Loop Visual -->
            <div class="mt-8 flex justify-center">
                <div class="bg-blue-50 border border-blue-200 text-blue-800 px-6 py-3 rounded-full text-sm font-semibold flex items-center">
                    <span class="mr-2">↺</span> Feedback Loop: Auto-Adjustment of Control Parameters
                </div>
            </div>
        </section>

        <!-- SECTION 3: KEY PERFORMANCE INDICATORS (KPIs) -->
        <section>
            <div class="text-center mb-12">
                <h3 class="text-3xl font-bold text-slate-800">Critical Success Metrics</h3>
                <p class="text-slate-600 mt-2">
                    The project aims to achieve domestic firsts in accuracy and significant efficiency gains.
                </p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                
                <!-- KPI Description -->
                <div class="space-y-6">
                    <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
                        <h4 class="text-xl font-bold text-blue-700 mb-2">Target Accuracy: 90%+</h4>
                        <p class="text-slate-600 text-sm">
                            The core goal is to achieve over 90% accuracy in the virtual soft sensor's predictions compared to physical reference standards, a first for domestic pyrolysis technology.
                        </p>
                    </div>
                    <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
                        <h4 class="text-xl font-bold text-cyan-600 mb-2">Energy Cost Reduction: ~30%</h4>
                        <p class="text-slate-600 text-sm">
                            By optimizing the heat process and reducing waste, the system supports the government's Carbon Neutrality Innovation Strategy.
                        </p>
                    </div>
                </div>

                <!-- KPI Charts -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <!-- Gauge Chart (Donut) -->
                    <div class="bg-white p-6 rounded-xl shadow-lg flex flex-col items-center">
                        <h5 class="text-sm font-bold text-slate-500 mb-4 uppercase">Sensor Accuracy Goal</h5>
                        <div class="chart-container" style="height: 200px; max-height: 200px;">
                            <canvas id="accuracyChart"></canvas>
                        </div>
                        <p class="text-3xl font-extrabold text-blue-600 mt-[-40px] z-10">90%</p>
                    </div>

                    <!-- Bar Chart (Cost) -->
                    <div class="bg-white p-6 rounded-xl shadow-lg flex flex-col items-center">
                        <h5 class="text-sm font-bold text-slate-500 mb-4 uppercase">Energy Cost Savings</h5>
                        <div class="chart-container" style="height: 200px; max-height: 200px;">
                            <canvas id="costChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION 4: DEEP DIVE - PROCESS OPTIMIZATION (Plotly 3D) -->
        <section>
             <div class="text-left md:text-center mb-8">
                <h3 class="text-3xl font-bold text-slate-800">The Optimization Landscape</h3>
                <p class="text-slate-600 mt-2 max-w-3xl mx-auto">
                    Visualizing how the control system finds the "sweet spot" for material yield by balancing 
                    Temperature and Pressure. (Conceptual Representation)
                </p>
            </div>
            
            <div class="bg-white rounded-2xl shadow-xl p-4 md:p-8 border border-slate-200">
                <!-- Plotly Container -->
                <div id="plotlyDiv" class="w-full h-[500px]"></div>
                <div class="mt-4 text-center text-sm text-slate-500">
                    *Interactive 3D Surface Plot: Rotate to explore the relationship between Temperature, Pressure, and Predicted Yield.*
                </div>
            </div>
        </section>

        <!-- SECTION 5: MARKET & IMPACT -->
        <section class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <!-- Market Context -->
            <div class="lg:col-span-1 bg-gradient-to-br from-slate-800 to-slate-900 text-white rounded-2xl p-8 shadow-2xl flex flex-col justify-center">
                <h3 class="text-2xl font-bold mb-6">Why It Matters</h3>
                <p class="mb-6 text-slate-300 leading-relaxed">
                    Process heat accounts for a massive portion of manufacturing energy. Optimizing this single factor is the most direct path to carbon neutrality in heavy industry.
                </p>
                <div class="border-t border-slate-700 pt-6">
                    <p class="text-4xl font-bold text-cyan-400 mb-2">60%</p>
                    <p class="text-sm text-slate-400">of Manufacturing Energy Consumption is Process Heat</p>
                </div>
            </div>

            <!-- Energy Breakdown Chart -->
            <div class="lg:col-span-1 bg-white rounded-2xl p-8 shadow-lg border border-slate-100">
                <h5 class="text-sm font-bold text-slate-500 mb-6 uppercase text-center">Industrial Energy Usage</h5>
                <div class="chart-container">
                    <canvas id="energyPieChart"></canvas>
                </div>
            </div>

            <!-- Application Fields -->
            <div class="lg:col-span-1 bg-white rounded-2xl p-8 shadow-lg border border-slate-100 flex flex-col">
                <h5 class="text-sm font-bold text-slate-500 mb-6 uppercase">Target Industries</h5>
                <div class="flex-grow space-y-4">
                    <div class="flex items-center p-3 bg-blue-50 rounded-lg">
                        <span class="text-2xl mr-3">🔋</span>
                        <span class="font-semibold text-slate-700">Secondary Battery</span>
                    </div>
                    <div class="flex items-center p-3 bg-cyan-50 rounded-lg">
                        <span class="text-2xl mr-3">♻️</span>
                        <span class="font-semibold text-slate-700">Upcycling & Biomass</span>
                    </div>
                    <div class="flex items-center p-3 bg-indigo-50 rounded-lg">
                        <span class="text-2xl mr-3">⚗️</span>
                        <span class="font-semibold text-slate-700">Petrochemical Plant</span>
                    </div>
                    <div class="flex items-center p-3 bg-slate-50 rounded-lg">
                        <span class="text-2xl mr-3">💾</span>
                        <span class="font-semibold text-slate-700">Semiconductor</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION 6: TIMELINE & BUDGET -->
        <section class="mb-20">
            <div class="text-center mb-12">
                <h3 class="text-3xl font-bold text-slate-800">Project Roadmap</h3>
                <p class="text-slate-600 mt-2">
                    A 33-month intensive R&D journey backed by 4.015 Billion KRW in government support.
                </p>
            </div>

            <div class="bg-white rounded-2xl shadow-xl overflow-hidden">
                <div class="grid grid-cols-1 md:grid-cols-2">
                    <!-- Timeline Visual -->
                    <div class="p-8 md:p-12 bg-slate-50">
                        <h4 class="font-bold text-xl text-slate-800 mb-8">Development Phases</h4>
                        <div class="relative border-l-2 border-blue-200 ml-3 space-y-10">
                            
                            <!-- Year 1 -->
                            <div class="relative pl-8">
                                <div class="absolute -left-[9px] top-0 w-4 h-4 rounded-full bg-blue-500 ring-4 ring-blue-100"></div>
                                <h5 class="font-bold text-blue-600">Year 1 (9 Months)</h5>
                                <p class="text-sm text-slate-600 mt-1">Data collection methodology & AI Model Foundation.</p>
                            </div>

                            <!-- Year 2 -->
                            <div class="relative pl-8">
                                <div class="absolute -left-[9px] top-0 w-4 h-4 rounded-full bg-cyan-500 ring-4 ring-cyan-100"></div>
                                <h5 class="font-bold text-cyan-600">Year 2 (12 Months)</h5>
                                <p class="text-sm text-slate-600 mt-1">Soft Sensor Pack Development & Simulation Integration.</p>
                            </div>

                            <!-- Year 3 -->
                            <div class="relative pl-8">
                                <div class="absolute -left-[9px] top-0 w-4 h-4 rounded-full bg-indigo-500 ring-4 ring-indigo-100"></div>
                                <h5 class="font-bold text-indigo-600">Year 3 (12 Months)</h5>
                                <p class="text-sm text-slate-600 mt-1">Integrated Control System Realization & On-site Verification.</p>
                            </div>
                        </div>
                    </div>

                    <!-- Budget Chart -->
                    <div class="p-8 md:p-12">
                        <h4 class="font-bold text-xl text-slate-800 mb-6">Funding Allocation</h4>
                        <div class="chart-container">
                            <canvas id="budgetChart"></canvas>
                        </div>
                        <p class="text-xs text-right text-slate-400 mt-2">*Unit: 100 Million KRW</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- FOOTER -->
        <footer class="text-center text-slate-400 py-12 border-t border-slate-200">
            <p>&copy; 2026 Industrial Convergence Technology - Strategic Infographic</p>
            <p class="text-sm mt-2">Source: RFP No. 2026-Industrial-Convergence-Item-General-08</p>
        </footer>

    </main>

    <!-- SCRIPTS -->
    <script>
        // --- UTILITIES ---
        
        // 1. Label Wrapping Helper (16 char limit)
        function wrapLabel(str, maxLen = 16) {
            if (str.length <= maxLen) return str;
            const words = str.split(' ');
            const lines = [];
            let currentLine = words[0];

            for (let i = 1; i < words.length; i++) {
                if (currentLine.length + 1 + words[i].length <= maxLen) {
                    currentLine += ' ' + words[i];
                } else {
                    lines.push(currentLine);
                    currentLine = words[i];
                }
            }
            lines.push(currentLine);
            return lines;
        }

        // 2. Global Chart.js Defaults
        Chart.defaults.font.family = "'Inter', sans-serif";
        Chart.defaults.color = '#64748B';
        Chart.defaults.responsive = true;
        Chart.defaults.maintainAspectRatio = false;

        // Tooltip Callback for Multi-line Labels
        const tooltipPlugin = {
            callbacks: {
                title: function(tooltipItems) {
                    const item = tooltipItems[0];
                    let label = item.chart.data.labels[item.dataIndex];
                    if (Array.isArray(label)) {
                        return label.join(' ');
                    } else {
                        return label;
                    }
                }
            }
        };

        // --- CHART 1: ACCURACY GAUGE (DONUT) ---
        const ctxAccuracy = document.getElementById('accuracyChart').getContext('2d');
        new Chart(ctxAccuracy, {
            type: 'doughnut',
            data: {
                labels: ['Target Accuracy', 'Gap'],
                datasets: [{
                    data: [90, 10],
                    backgroundColor: ['#2563EB', '#E2E8F0'], // Blue 600, Slate 200
                    borderWidth: 0,
                    hoverOffset: 4
                }]
            },
            options: {
                cutout: '75%',
                plugins: {
                    legend: { display: false },
                    tooltip: tooltipPlugin
                }
            }
        });

        // --- CHART 2: COST REDUCTION BAR ---
        const ctxCost = document.getElementById('costChart').getContext('2d');
        new Chart(ctxCost, {
            type: 'bar',
            data: {
                labels: wrapLabel('Traditional Process vs Optimized Smart Process').concat(wrapLabel('Energy Efficiency Gain')),
                // Note: Providing dummy structure for simple comparison
                labels: [wrapLabel('Current Energy Cost'), wrapLabel('Optimized Cost')],
                datasets: [{
                    label: 'Relative Cost Index',
                    data: [100, 70], // 30% reduction
                    backgroundColor: ['#94A3B8', '#06B6D4'], // Slate 400, Cyan 500
                    borderRadius: 8,
                    barPercentage: 0.6
                }]
            },
            options: {
                scales: {
                    y: { beginAtZero: true, display: false },
                    x: { grid: { display: false } }
                },
                plugins: {
                    legend: { display: false },
                    tooltip: tooltipPlugin
                }
            }
        });

        // --- CHART 3: ENERGY USAGE PIE ---
        const ctxPie = document.getElementById('energyPieChart').getContext('2d');
        new Chart(ctxPie, {
            type: 'pie',
            data: {
                labels: [wrapLabel('Process Heat'), wrapLabel('Motor Power'), wrapLabel('Lighting & Others')],
                datasets: [{
                    data: [60, 25, 15],
                    backgroundColor: [
                        '#7C3AED', // Violet 600 (Main Focus)
                        '#A78BFA', // Violet 400
                        '#DDD6FE'  // Violet 200
                    ],
                    borderWidth: 2,
                    borderColor: '#ffffff'
                }]
            },
            options: {
                plugins: {
                    legend: { position: 'bottom', labels: { usePointStyle: true, boxWidth: 10 } },
                    tooltip: tooltipPlugin
                }
            }
        });

        // --- CHART 4: BUDGET (STACKED BAR/TIMELINE) ---
        const ctxBudget = document.getElementById('budgetChart').getContext('2d');
        new Chart(ctxBudget, {
            type: 'bar',
            data: {
                labels: ['Year 1', 'Year 2', 'Year 3'],
                datasets: [{
                    label: 'Gov Support (Approx)',
                    data: [10.95, 14.6, 14.6], // 10.95 fixed, split remainder of 40.15 evenly for vis
                    backgroundColor: '#3B82F6',
                    borderRadius: 6
                }]
            },
            options: {
                scales: {
                    y: { 
                        beginAtZero: true,
                        grid: { borderDash: [5, 5] },
                        title: { display: true, text: '100 Million KRW' }
                    },
                    x: { grid: { display: false } }
                },
                plugins: {
                    legend: { display: false },
                    tooltip: tooltipPlugin
                }
            }
        });

        // --- CHART 5: PLOTLY 3D SURFACE (OPTIMIZATION LANDSCAPE) ---
        // Generates a mock "Hill Climbing" optimization surface
        
        // Data Generation
        const size = 25;
        const x = new Array(size).fill(0).map((_, i) => i); // Temp
        const y = new Array(size).fill(0).map((_, i) => i); // Pressure
        const z = []; // Yield

        for (let i = 0; i < size; i++) {
            const row = [];
            for (let j = 0; j < size; j++) {
                // Create a peak function (Gaussian-ish)
                const dist = Math.sqrt(Math.pow(i - 12, 2) + Math.pow(j - 12, 2));
                const val = 95 * Math.exp(-dist / 10) + (Math.random() * 2); // Peak at 95% yield
                row.push(val);
            }
            z.push(row);
        }

        const data3D = [{
            z: z,
            x: x,
            y: y,
            type: 'surface',
            colorscale: 'Viridis', // Vibrant colors
            showscale: false,
            opacity: 0.9,
            contours: {
                z: { show: true, usecolormap: true, highlightcolor: "#42f546", project: { z: true } }
            }
        }];

        const layout3D = {
            autosize: true,
            margin: { l: 0, r: 0, b: 0, t: 0 },
            scene: {
                xaxis: { title: 'Temp' },
                yaxis: { title: 'Pressure' },
                zaxis: { title: 'Yield (%)' },
                camera: { eye: { x: 1.5, y: 1.5, z: 1.5 } }
            },
            paper_bgcolor: 'rgba(0,0,0,0)',
            plot_bgcolor: 'rgba(0,0,0,0)'
        };

        // Render Plotly
        Plotly.newPlot('plotlyDiv', data3D, layout3D, {displayModeBar: false, responsive: true});

    </script>
</body>
</html>