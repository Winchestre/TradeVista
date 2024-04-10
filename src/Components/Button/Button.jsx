export default function Button({ label, color }) {
    return <button style={{backgroundColor: color}} className="px-6 py-2 text-white rounded-sm">{label}</button>
}