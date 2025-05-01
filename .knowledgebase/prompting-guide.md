## A Guide to Crafting Effective AI Prompts

This guide explains how to create high-quality prompts for Large Language Models (LLMs), focusing on two primary types: Chat Prompts and Agent Prompts. Understanding the distinction and the necessary components for each is crucial for eliciting desired behavior and capabilities from an AI.

**Target Audience:** This guide is intended for an AI learning to generate and refine prompts, particularly complex Agent Prompts.

### Section 1: Crafting Effective Chat Prompts

**Purpose:** Chat prompts typically set the stage for a *specific*, often shorter, interaction. They establish an initial persona, context, and goal for the conversation but usually don't define complex, multi-step behaviors or tool use in the same depth as agent prompts.

**Key Elements of a Chat Prompt:**

1.  **Role/Persona (Simplified):**
    *   **What:** Briefly define the AI's role for this specific chat.
    *   **Why:** Sets the tone and expertise level expected.
    *   **Best Practice Example:** `You are a cybersecurity expert explaining the concept of SQL injection.`

2.  **Task/Goal:**
    *   **What:** Clearly state the primary objective of the *current* conversation.
    *   **Why:** Focuses the AI on the immediate user need.
    *   **Best Practice Example:** `Your goal is to explain SQL injection, provide a simple code example of a vulnerable query, and suggest one primary mitigation technique.`

3.  **Context:**
    *   **What:** Provide essential background information relevant *only* to the current task.
    *   **Why:** Gives the AI the necessary details to provide a relevant answer.
    *   **Best Practice Example:** `The user is a junior web developer with basic knowledge of SQL but is unfamiliar with security vulnerabilities.`

4.  **Constraints/Format:**
    *   **What:** Specify desired output characteristics like length, style, or specific elements to include/exclude.
    *   **Why:** Ensures the response meets the user's presentation needs.
    *   **Best Practice Example:** `Limit the explanation to 200 words. Use a code block for the example. Present the mitigation technique as a single bullet point. Avoid overly technical terms.`

5.  **Tone:**
    *   **What:** Define the desired conversational style (e.g., formal, friendly, technical, encouraging).
    *   **Why:** Shapes the user experience.
    *   **Best Practice Example:** `Adopt an informative and slightly formal, yet accessible, tone.`

**When to Use:** Chat prompts are best for Q&A, simple content generation, explanations, or focused tasks where the AI doesn't need persistent state, complex tool interactions, or a deeply defined identity across multiple turns.

---

### Section 2: Engineering Robust Agent Prompts

**Purpose:** Agent prompts define the **identity, capabilities, rules, and persistent behavior** of an AI designed to perform complex, multi-step tasks, often involving interaction with external tools, filesystems, or APIs. These prompts are foundational blueprints for agentic systems.

**Key Components of an Agent Prompt:**

1.  **Core Identity & Purpose:**
    *   **What:** Define *who* the agent is (its name/designation) and its overarching *mission* or primary function. This is more enduring than a chat persona.
    *   **Why:** Establishes the agent's fundamental reason for existence and guides its overall behavior.
    *   **Best Practice Example:** `You are 'CodeCrafter', an AI assistant specializing in generating and refactoring Python code according to modern best practices. Your primary purpose is to help users write clean, efficient, and maintainable Python applications.`

2.  **Capabilities & Environment:**
    *   **What:** Detail *what* the agent can do, *where* it operates (specific IDE, a sandboxed Linux environment, etc.), what *tools* it has access to (with precise descriptions and schemas), and importantly, its *limitations*.
    *   **Why:** Clearly defines the agent's operational boundaries and available actions, preventing hallucinations about capabilities and ensuring it uses the correct tools within its environment.
    *   **Best Practice Examples:**
        *   `Environment: Operates within a containerized Ubuntu 22.04 environment with access to Python 3.10, Node.js 20, and standard system utilities. Internet access is enabled. No native GUI applications can be executed.`
        *   `Tool Limitation Example: The 'execute_command' tool cannot run commands requiring interactive user input during execution (e.g., prompts for 'y/n'). Structure commands to be non-interactive using flags like '-y' where possible.`
        *   `Forbidden Files Example: You are NOT allowed to modify files matching the pattern 'config/*.yaml' or any files within the '.git/' directory.`

3.  **Operating Principles & Rules (The "How"):**
    *   **What:** Provide explicit, detailed instructions on *how* the agent should perform its tasks. This is the most critical section for complex agents and should be highly structured. Break it down logically:
        *   **General Workflow/Loop:** Describe the agent's operational cycle.
            *   **Best Practice Example:** `Follow this execution cycle: 1. Analyze Events (prioritize user messages, review tool results). 2. Plan Next Step (identify the goal and necessary information). 3. Select & Explain Tool (choose the best tool, explain rationale to the user). 4. Execute Tool. 5. Wait for Observation. 6. Repeat until task completion or user stop request.`
        *   **Tool Usage:** Define strict rules for calling tools.
            *   **Best Practice Example:** `<tool_usage_rules> Always validate parameters against the provided JSON schema before calling a tool. If a tool call fails, analyze the error message. First, retry with corrected parameters if applicable. If failure persists, attempt an alternative tool or strategy. If all alternatives fail, report the failure and the attempted steps clearly to the user. Never mention internal tool names (e.g., 'read_file_tool') in user-facing communication; describe the action instead (e.g., 'I will read the file'). </tool_usage_rules>`
        *   **Information Gathering:** Specify strategies for acquiring context.
            *   **Best Practice Example:** `When researching, prioritize information from official documentation (if available via tools or web search) over general web search results. If conflicting information is found, attempt to cross-verify using a third source or explicitly state the discrepancy to the user. Read relevant sections of a file using 'read_file_chunk' before attempting edits with 'apply_edit'.`
        *   **Code Modification:** Detail rules for editing/creating code.
            *   **Best Practice Example:** `<code_modification_rules> Ensure all generated code includes necessary imports and adheres to the project's established style (e.g., PEP 8 for Python). Before applying an edit, read the target code section unless creating a new file or appending a trivial change. Edits should be idempotent where possible. When using an 'apply_edit' tool that requires placeholders for unchanged code (e.g., '{{...}}' or '// ... existing code ...'), use them consistently to represent *all* unmodified sections between changes. ALWAYS validate code changes by running linters or tests if available via tools. Fix errors introduced by your edits before concluding the task. </code_modification_rules>`
        *   **Communication Style:** Define how the agent interacts with the user.
            *   **Best Practice Example:** `Communicate concisely and professionally. Avoid filler phrases. If user instructions are ambiguous, use the 'ask_clarification' tool with specific, targeted questions rather than making assumptions. Present complex information or plans using structured Markdown (bullet points, numbered lists).`
        *   **Data Handling & Security:** Outline rules for dealing with sensitive data, secrets, databases.
            *   **Best Practice Example:** `Never request passwords or highly sensitive PII. If API keys or secrets are required, use the dedicated 'request_secret' tool. Never hardcode secrets directly into code or configuration files. When interacting with databases, default to read-only operations unless modification is explicitly requested and necessary for the task. Avoid destructive commands (DROP, DELETE without WHERE) unless specifically confirmed by the user after a warning.`
        *   **Planning & Debugging:** Instruct the agent on how to plan tasks and troubleshoot issues.
            *   **Best Practice Example:** `For multi-step tasks, first outline the plan using Markdown (e.g., numbered steps) before executing the first step. When debugging, add detailed logging statements around the suspected faulty code section. Use available tools to run the code and inspect the logs. Isolate the issue before attempting a fix.`
        *   **Framework/Technology Specifics:** Provide guidelines for specific tech stacks.
            *   **Best Practice Example:** `When working with React, prioritize functional components and Hooks. Utilize the provided UI component library (e.g., Shadcn/UI via '@/') before creating custom components. Ensure components are responsive using Tailwind CSS utility classes.`
    *   **Why:** These rules govern the agent's decision-making process at every step, ensuring consistency, safety, efficiency, and adherence to best practices. Granularity is key.

4.  **Structure & Formatting:**
    *   **What:** Define how the prompt itself is organized. Use headings, bullet points, or custom tags (like `<tool_usage_rules>`, `<code_modification_rules>`) to logically group instructions. Specify required output formats (e.g., Markdown, JSON for tool arguments).
    *   **Why:** Structure improves readability and helps the underlying model parse and adhere to complex instructions more reliably.
    *   **Best Practice Example:**
        ```
        # Core Identity
        You are 'DataAnalyzer', an AI assistant focused on data processing...

        # Capabilities
        <tools>
          <tool name="read_csv">...</tool>
          <tool name="run_python_script">...</tool>
        </tools>
        <environment>...</environment>

        # Operating Principles
        <data_handling_rules>
          - Always infer data types initially, but allow user override.
          - Handle missing values using mean imputation by default...
        </data_handling_rules>
        <communication_rules>
          - Present results using Markdown tables...
        </communication_rules>

        # Context Injection
        User's current working directory: ${cwd}
        Available data files: ${file_list}
        ```

5.  **Context Injection:**
    *   **What:** Explain how dynamic, run-time information (like current working directory, OS, available files, environment variables, user info) will be provided to the agent (often via placeholders like `${cwd}` or specific tagged sections).
    *   **Why:** Allows the agent to operate with awareness of its current, specific context.

6.  **Examples & Refusals:**
    *   **What:** Include concrete examples of desired behavior, tool usage, or output formats. Provide explicit instructions and phrasing for refusing harmful or inappropriate requests.
    *   **Why:** Examples clarify complex instructions. Clear refusal guidelines ensure safety and alignment.
    *   **Best Practice Example (Refusal):** `If the user asks for harmful, unethical, or illegal content, respond ONLY with the text: "I cannot fulfill that request." Do not apologize or explain further.`

7.  **Memory/Persistence (If Applicable):**
    *   **What:** If the agent has access to a memory system (like a `save_context` tool), instruct it on *when* and *what* to remember.
    *   **Why:** Enables the agent to retain important context beyond its immediate context window for long-running tasks or user preferences.
    *   **Best Practice Example:** `Use the 'save_memory' tool to record: user-stated preferences (e.g., 'always use tabs for indentation'), key architectural decisions made during the session, and summaries of successfully completed sub-tasks in a long project. Title memories clearly (e.g., 'User Preference: Indentation').`

**Process for Creating/Enhancing Agent Prompts:**

1.  **Define Goal & Scope:** What is the agent's primary function? What tasks will it perform?
2.  **Specify Environment & Tools:** Where does it run? What tools does it need? What are the hard constraints?
3.  **Establish Identity:** Give it a name and define its core purpose.
4.  **Detail Operating Principles:** This is the core. For *each* major function (communicating, editing code, using tools, searching, planning, etc.), write explicit, step-by-step rules. Use the components listed above as a checklist. Be exhaustive.
5.  **Structure the Prompt:** Organize instructions logically using headings or tags for clarity.
6.  **Provide Examples:** Illustrate complex rules or desired outputs with concrete examples.
7.  **Add Safety Layers:** Include clear refusal instructions. Define safety protocols for tools.
8.  **Consider Persistence:** If needed, define rules for using a memory system.
9.  **Test & Iterate:** Agent prompting is iterative. Test the agent, observe its behavior, and refine the prompt (especially the Operating Principles) to address shortcomings or add new capabilities.

**Enhancing Existing Agent Prompts:**

*   **Identify the Issue:** Is the agent failing to use a tool correctly? Is its communication style off? Is it making unsafe edits?
*   **Locate Relevant Section:** Find the part of the prompt governing that behavior (e.g., a section tagged `<tool_usage_rules>`, `<communication_rules>`, or similar).
*   **Refine Instructions:** Make the rules in that section more explicit, add constraints, provide clearer examples, or correct faulty logic based on the observed failure.
*   **Add New Capabilities:** Introduce new tools by adding their descriptions/schemas to the Capabilities section and defining usage rules in the Operating Principles. Add new behavioral rules as needed.
*   **Test:** Verify that the enhancement fixed the issue or added the capability without negatively impacting other behaviors.

**Conclusion:**

Crafting prompts, especially for complex agents, is a form of engineering. It requires clarity, structure, precision, and an iterative approach. Chat prompts set the stage, while Agent Prompts build the entire character, defining *what* it is, *what* it can do, and *how* it must behave to successfully and safely accomplish its mission. By carefully constructing each component with clear rules and best practices, you can guide the AI to perform sophisticated tasks reliably.